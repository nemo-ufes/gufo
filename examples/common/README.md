# Shared assets

Files used by every example in `examples/`:

* `style.css` -- stylesheet for the tutorial pages, extending `docs/style.css` from
  the main gUFO documentation with a few additions for the tutorial format (concept
  badges, callouts, numbered steps).
* `gufoshapes.ttl` -- vendored copy of the SHACL shapes from
  [nemo-ufes/gufoshapes](https://github.com/nemo-ufes/gufoshapes), used to validate
  each example's use of gUFO's taxonomy of types. See the header of the file for the
  exact commit it was fetched from. To refresh it:

      curl -s -o examples/common/gufoshapes.ttl \
        https://raw.githubusercontent.com/nemo-ufes/gufoshapes/main/gufoshapes.ttl

  (then re-add the provenance header that is stripped by the raw fetch).

The examples themselves reference `gufo.ttl` at the root of this repository rather
than a vendored copy, so they always exercise the version of gUFO checked out in the
working tree.
