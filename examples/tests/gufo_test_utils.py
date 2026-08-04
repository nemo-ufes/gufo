"""Shared helpers for validating the gUFO usage examples.

Two kinds of checks are used throughout this test suite:

* OWL 2 DL reasoning (consistency and classification) with the Pellet reasoner,
  run through owlready2. This catches logical contradictions -- e.g. an
  individual that would have to belong to two disjoint classes.
* SHACL validation against the gUFO shapes from
  https://github.com/nemo-ufes/gufoshapes (vendored in examples/common/). This
  catches taxonomic mistakes that are *not* logical contradictions in OWL --
  most notably, misuses of gUFO's taxonomy of types (rigid types specializing
  anti-rigid types, sortals without an identity provider, powertype pattern
  violations, etc). OWL 2 punning makes these invisible to a DL reasoner, which
  is precisely why the SHACL shapes exist.
"""
from __future__ import annotations

import tempfile
from pathlib import Path

import owlready2
import rdflib

REPO_ROOT = Path(__file__).resolve().parents[2]
EXAMPLES_ROOT = REPO_ROOT / "examples"
GUFO_TTL = REPO_ROOT / "gufo.ttl"
GUFOSHAPES_TTL = EXAMPLES_ROOT / "common" / "gufoshapes.ttl"


def discover_examples() -> list[Path]:
    """Return the example directories, sorted, that contain an ontology.ttl."""
    return sorted(
        p.parent for p in EXAMPLES_ROOT.glob("*/ontology.ttl") if p.is_file()
    )


def load_graph(*paths: Path) -> rdflib.Graph:
    graph = rdflib.Graph()
    for path in paths:
        graph.parse(path, format="turtle")
    return graph


class Inconsistent(Exception):
    pass


def run_owl_reasoning(*ttl_paths: Path):
    """Load the given turtle files together and classify with Pellet.

    Returns the owlready2 ontology object (post-reasoning) so callers can
    inspect inferred types/classification. Raises Inconsistent if Pellet
    finds the merged ontology inconsistent.
    """
    graph = load_graph(*ttl_paths)

    with tempfile.TemporaryDirectory() as tmp:
        owl_file = Path(tmp) / "merged.owl"
        graph.serialize(destination=str(owl_file), format="xml")

        # owlready2 needs its own World per reasoning run, otherwise repeated
        # test invocations accumulate entities across unrelated examples.
        world = owlready2.World()
        onto = world.get_ontology(f"file://{owl_file}").load()

        try:
            owlready2.sync_reasoner_pellet(
                world,
                infer_property_values=False,
                infer_data_property_values=False,
                debug=0,
            )
        except owlready2.OwlReadyInconsistentOntologyError as exc:
            raise Inconsistent(str(exc)) from exc

        return world, onto


def unsatisfiable_classes(world: owlready2.World) -> list:
    """Classes forced to be equivalent to owl:Nothing after classification."""
    nothing = owlready2.Nothing
    return [
        c
        for c in world.classes()
        if c is not nothing and nothing in c.equivalent_to
    ]


def run_shacl(*data_ttl_paths: Path, shapes_path: Path = GUFOSHAPES_TTL):
    import pyshacl

    data_graph = load_graph(*data_ttl_paths)
    shapes_graph = rdflib.Graph()
    shapes_graph.parse(shapes_path, format="turtle")

    conforms, report_graph, report_text = pyshacl.validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference="none",
        advanced=True,
    )
    return conforms, report_text
