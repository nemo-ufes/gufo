# Testing the examples

Each example under `examples/` is checked two ways:

1. **OWL 2 DL reasoning** with the [Pellet](https://github.com/stardog-union/pellet)
   reasoner (bundled with [owlready2](https://owlready2.readthedocs.io/), driven
   through a local JVM -- no network access needed at test time). This confirms
   that `gufo.ttl` plus the example's `ontology.ttl` is logically consistent, and
   that reasoning does not force any class to be unsatisfiable.

   (Pellet, rather than HermiT, is used here because gUFO's temporal data
   properties use `xsd:date`, which is outside HermiT's built-in OWL 2 datatype
   map; Pellet handles it without complaint.)

2. **SHACL validation** with [pySHACL](https://github.com/RDFLib/pySHACL) against
   the gUFO shapes vendored in `examples/common/gufoshapes.ttl` (from
   [nemo-ufes/gufoshapes](https://github.com/nemo-ufes/gufoshapes)). This is what
   catches taxonomic mistakes -- e.g. a `gufo:Kind` specializing a `gufo:Role` --
   that OWL 2 punning hides from a DL reasoner and that step 1 will therefore
   *not* catch. Some examples (01 and 07) ship an `invalid-example.ttl` file that
   intentionally makes such a mistake, precisely to demonstrate this gap: the
   tests assert that it stays OWL-consistent yet still gets flagged by SHACL.

## Running

Requires Python 3.9+ and a JVM on `PATH` (Pellet and HermiT are Java tools; only
Pellet is used here). Both `rdflib`/`pyshacl`/`owlready2` and their reasoners are
installed from PyPI -- no other setup is required.

```sh
cd examples/tests
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pytest -v
```

New examples are picked up automatically: any `examples/*/ontology.ttl` is
included in the consistency and SHACL checks, and any accompanying
`invalid-example.ttl` is checked as a negative case.
