# gUFO usage examples

Seven small, realistic ontologies that each illustrate one part of gUFO's foundations, paired with a
tutorial-style HTML page. Start at [`index.html`](index.html) -- clone the repository and open it in a
browser (GitHub renders `.html` files as plain text rather than as pages).

| # | Example | Domain | gUFO concepts |
|---|---------|--------|----------------|
| 1 | [Endurant types](01-endurant-types/) | People & organizations | `Kind`, `SubKind`, `Phase`, `Role`, `Category`, `RoleMixin`, `PhaseMixin` |
| 2 | [Objects and their parts](02-objects-and-parts/) | Car fleet | `FunctionalComplex`, `Collection`, `Quantity` and their part-whole properties |
| 3 | [Qualities and quality values](03-qualities/) | Retail products | `Quality`, `QualityValue`, basic / enumerated / multidimensional value patterns |
| 4 | [Relators and extrinsic aspects](04-relators/) | Employment & marriage | `Relator`, `mediates`, `ExtrinsicMode`, `MaterialRelationshipType` |
| 5 | [Events](05-events/) | Football tournament | `Event`, `participatedIn`, `historicallyDependsOn`, `wasCreatedIn`/`wasTerminatedIn`, `manifestedIn` |
| 6 | [Situations](06-situations/) | Patient health record | All five `Situation` subclasses, `broughtAbout`, `contributedToTrigger` |
| 7 | [Higher-order types](07-higher-order-types/) | Wildlife classification | `categorizes`, `partitions` (the powertype pattern) |

Examples 1 and 7 additionally ship an `invalid-example.ttl`: a deliberate misuse of gUFO that stays
OWL-consistent but is rejected by the SHACL shapes, used to show why the shapes are needed on top of a DL
reasoner.

## Layout

```
examples/
  index.html               landing page linking all seven examples
  common/                  shared stylesheet and vendored gufoshapes.ttl (see common/README.md)
  01-endurant-types/
    ontology.ttl           the example ontology (imports gufo.ttl)
    invalid-example.ttl     a deliberate misuse, for contrast
    index.html              the tutorial
  02-objects-and-parts/
    ontology.ttl
    index.html
  ... (03-qualities, 04-relators, 05-events, 06-situations, 07-higher-order-types follow the same shape)
  tests/                    pytest suite validating every ontology.ttl (see tests/README.md)
```

## Testing

Every `ontology.ttl` is validated with an OWL 2 DL reasoner (Pellet, via owlready2 -- consistency and
classification) and with SHACL ([pySHACL](https://github.com/RDFLib/pySHACL) against the
[gUFO SHACL shapes](https://github.com/nemo-ufes/gufoshapes), vendored in `common/gufoshapes.ttl`). See
[`tests/README.md`](tests/README.md) for details and how to run it:

```sh
cd examples/tests
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pytest -v
```
