"""Validates every gUFO usage example under examples/ with:

1. an OWL 2 DL reasoner (Pellet, via owlready2) -- checks that gufo.ttl plus the
   example's ontology.ttl is logically consistent and that no class is forced
   unsatisfiable; and
2. the gUFO SHACL shapes (github.com/nemo-ufes/gufoshapes) -- checks that the
   example follows the taxonomic rules of gUFO's taxonomy of types that OWL
   punning cannot enforce on its own.

Run with:

    cd examples/tests
    python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
    .venv/bin/pytest -v
"""
from __future__ import annotations

import pytest

import gufo_test_utils as u

EXAMPLES = u.discover_examples()
EXAMPLE_IDS = [p.name for p in EXAMPLES]

INVALID_EXAMPLES = sorted(
    p.parent for p in u.EXAMPLES_ROOT.glob("*/invalid-example.ttl")
)
INVALID_IDS = [p.name for p in INVALID_EXAMPLES]


def test_examples_were_discovered():
    assert EXAMPLES, f"No examples found under {u.EXAMPLES_ROOT}"


@pytest.mark.parametrize("example", EXAMPLES, ids=EXAMPLE_IDS)
def test_ontology_ttl_parses(example):
    graph = u.load_graph(example / "ontology.ttl")
    assert len(graph) > 0


@pytest.mark.parametrize("example", EXAMPLES, ids=EXAMPLE_IDS)
def test_example_is_owl_consistent_and_satisfiable(example):
    ontology_ttl = example / "ontology.ttl"
    try:
        world, onto = u.run_owl_reasoning(u.GUFO_TTL, ontology_ttl)
    except u.Inconsistent as exc:
        pytest.fail(
            f"{example.name}: gufo.ttl + ontology.ttl is OWL-inconsistent "
            f"according to Pellet:\n{exc}"
        )
    unsatisfiable = u.unsatisfiable_classes(world)
    assert not unsatisfiable, (
        f"{example.name}: the following classes were classified as "
        f"unsatisfiable (equivalent to owl:Nothing): {unsatisfiable}"
    )


@pytest.mark.parametrize("example", EXAMPLES, ids=EXAMPLE_IDS)
def test_example_conforms_to_gufo_shapes(example):
    ontology_ttl = example / "ontology.ttl"
    conforms, report_text = u.run_shacl(u.GUFO_TTL, ontology_ttl)
    assert conforms, (
        f"{example.name}: ontology.ttl does not conform to the gUFO SHACL "
        f"shapes:\n{report_text}"
    )


@pytest.mark.parametrize("example", INVALID_EXAMPLES, ids=INVALID_IDS)
def test_invalid_example_is_flagged_by_shapes(example):
    """invalid-example.ttl files intentionally misuse gUFO; the SHACL shapes
    must reject them even though (by design, see the docstring above) OWL
    alone is often unable to."""
    invalid_ttl = example / "invalid-example.ttl"
    conforms, report_text = u.run_shacl(u.GUFO_TTL, invalid_ttl)
    assert not conforms, (
        f"{example.name}: invalid-example.ttl was expected to violate the "
        f"gUFO SHACL shapes, but it conforms. Update the example or the "
        f"tutorial claim about what it demonstrates."
    )


@pytest.mark.parametrize("example", INVALID_EXAMPLES, ids=INVALID_IDS)
def test_invalid_example_is_still_owl_consistent(example):
    """Demonstrates *why* the SHACL shapes are needed: these particular
    mistakes are invisible to an OWL DL reasoner because of punning."""
    invalid_ttl = example / "invalid-example.ttl"
    try:
        u.run_owl_reasoning(u.GUFO_TTL, invalid_ttl)
    except u.Inconsistent as exc:
        pytest.fail(
            f"{example.name}: invalid-example.ttl was expected to remain "
            f"OWL-consistent (that's the point being illustrated -- OWL "
            f"punning hides this mistake from the reasoner), but Pellet "
            f"reported an inconsistency:\n{exc}"
        )
