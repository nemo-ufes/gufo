# gUFO: A Lightweight Implementation of the Unified Foundational Ontology (UFO)
 
The objective of gUFO is to provide a lightweight implementation of the Unified Foundational Ontology (UFO) [1-5] suitable for Semantic Web OWL 2 DL applications. 

Intended users are those implementing UFO-based lightweight ontologies that reuse gUFO by specializing and instantiating its elements.

There are three implications of the use of the term lightweight. First of all, we have employed little expressive means in an effort to retain computational properties for the resulting OWL ontology. Second, we have selected a subset of UFO-A [1, 2] and UFO-B [3] to include here. In particular, there is minimalistic support for UFO-B (only that which is necessary to establish the participation of objects in events and to capture historical dependence between events). Third, a lightweight ontology, differently from a reference ontology, is designed with the purpose of providing an implementation artifact to structure a knowledge base (or knowledge graph). This has driven a number of pragmatic implementation choices which are discussed in comments annotated to the various elements of this implementation. 

The 'g' in gUFO stands for gentle. At the same time, "gufo" is the Italian word for "owl".

For background information on the reference ontology on which this implementation is based, see: 

1. G. Guizzardi, G. Wagner, J. P. A. Almeida, R. S. S. Guizzardi, “Towards ontological foundations for conceptual modeling: The unified foundational ontology (UFO) story,” Applied Ontology (Online), vol. 10, p. 259–271, 2015. <http://dx.doi.org/10.3233/ao-150157>
2. G. Guizzardi, Ontological Foundations for Structural Conceptual Models,
PhD Thesis, University of Twente, The Netherlands, 2005. <https://research.utwente.nl/en/publications/ontological-foundations-for-structural-conceptual-models>
3. G. Guizzardi, G. Wagner, R. A. Falbo, R. S. S. Guizzardi, and J. P. A. Almeida, “Towards Ontological Foundations for the Conceptual Modeling of Events,” in Proc. 32th International Conference, ER 2013, 2013, p. 327–341. <https://doi.org/10.1007/978-3-642-41924-9_27>
4. G. Guizzardi, C. M. Fonseca, A. B. Benevides, J. P. A. Almeida, D. Porello, T. P. Sales, “Endurant Types in Ontology-Driven Conceptual Modeling: Towards OntoUML 2.0,” in Conceptual Modeling – 37th International Conference, ER 2018, 2018, p. 136–150. <https://doi.org/10.1007/978-3-030-00847-5_12>
5. C. M. Fonseca, D. Porello, G. Guizzardi, J. P. A. Almeida, and N. Guarino, “Relations in ontology-driven conceptual modeling,” in 38th International Conference on Conceptual Modeling (ER 2019), LNCS, 2019. v. 11788, 2019, p. 1–15. <http://dx.doi.org/10.1007/978-3-030-33223-5_4>

Authors:

* João Paulo A. Almeida;
* Giancarlo Guizzardi;
* Tiago Prince Sales;
* Ricardo A. Falbo.

See <http://purl.org/nemo/doc/gufo> for usage guide and complete documentation of gUFO.

Some tutorial videos can be found in: <https://www.youtube.com/channel/UCrO83sDDZ7q4ymI76bwB-bg>

To import gUFO in Protégé use <https://purl.org/nemo/gufo#> (using `https` instead of `http`). (This is required in Protégé 5.5.0 as it uses a version of the OWL API that is unable to handle multiple http redirects.)
