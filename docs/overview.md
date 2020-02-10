## Usage Guide <a name="usageguide"></a>

### Table of Contents

* 1\. [Usage Scenarios](#scenarios)
* 2\. [Taxonomy of Individuals](#individuals)
    * 2.1\. [Concrete Individuals](#concreteindividuals)
    * 2.2\. [Objects and their parts](#objectsandparts)
    * 2.3\. [Intrinsic Aspects](#intrinsicaspects)
    * 2.4\. [Qualities - Basic patterns](#basicqualities)
    * 2.5\. [Qualities - Advanced usage](#advancedqualities)
    * 2.6\. [Intrinsic Modes](#intrinsicmodes)
    * 2.7\. [Extrinsic Aspects](#extrinsicaspects)
    * 2.8\. [Events](#events)
    * 2.9\. [Situations](#situations)
* 3\. [Taxonomy of Types](#types)
    * 3.1\. [Endurant Types](#enduranttypes)
    * 3.2\. [Relationship Types](#relationshiptypes)
    * 3.3\. [Higher-Order Types](#highordertypes)

See also [reference table of contents](#toc).

<a name="scenarios"></a>

### 1. Usage Scenarios

gUFO is intended for reuse in the definition of UFO-based lightweight ontologies. The term "user" will thus be reserved to identify the designers of these ontologies.

Reuse of gUFO consists in instantiating and/or specializing the  various classes, object properties and data properties defined in the ontology, inheriting from it the domain-independent distinctions of UFO. This section provides an introduction to gUFO as a primer to prospective users. [Turtle](https://www.w3.org/TR/turtle/) is used as a syntax for RDF serialization for illustrative purposes.  

A key feature of UFO (and hence, gUFO) is that it includes two taxonomies: one with classes whose instances are individuals (classes in this taxonomy include gufo:Object, gufo:Event) and another with classes whose instances are types (classes in this taxonomy include gufo:Kind, gufo:Phase, gufo:Category).

An overview of these taxonomies in gUFO is shown below.

> * Individual
>     * AbstractIndividual
>     * ConcreteIndividual
>         * Endurant
>             * Object
>             * Aspect
>         * Event
>         * Situation
> * Type
>     * AbstractIndividualType
>     * ConcreteIndividualType
>         * EndurantType
>             * Sortal
>                 * Kind
>                 * Phase
>                 * Role
>                 * SubKind
>             * NonSortal
>                 * Category
>                 * PhaseMixin
>                 * RoleMixin
>                 * Mixin
>         * EventType
>         * SituationType
>     * RelationshipType

Considering these two taxonomies, the following usage scenarios are envisioned and discussed in this document  where appropriate:

1. A UFO-based ontology *instantiates* gUFO classes in the taxonomy of individuals  
   For example, `:Earth rdf:type gufo:Object` and `:WorldCup1970Final rdf:type gufo:Event`.
2. A UFO-based ontology *specializes* gUFO classes in the taxonomy of individuals  
   For example, `:Planet rdfs:subClassOf gufo:Object` and `:SoccerMatch rdfs:subClassOf gufo:Event`.
3. A UFO-based ontology *instantiates* gUFO classes in the taxonomy of types  
   For example, `:Planet rdf:type gufo:Kind`, `:Child rdf:type gufo:Phase`.
4. A UFO-based ontology *specializes* gUFO classes in the taxonomy of types  
   For example, `:PersonPhase rdfs:subClassOf gufo:Phase`.

Users may combine the various scenarios discussed. For example, users will often employ scenarios 2 and 3 in combination as shown in the following fragment, which defines a "Person" class that specializes gufo:Object and instantiates gufo:Kind:

    @prefix : <http://purl.org/nemo/example#> .
    @prefix gufo: <http://purl.org/nemo/gufo#> .

    :Person rdf:type owl:Class ;
            rdfs:subClassOf gufo:Object ;
            rdf:type gufo:Kind .

<a name="individuals"></a>

### 2. Taxonomy of Individuals

The taxonomy of individuals of gUFO has the following overall structure:

> * Individual
>     * AbstractIndividual
>     * ConcreteIndividual
>         * Endurant
>             * Object
>             * Aspect
>         * Event
>         * Situation

<a name="concreteindividuals"></a>

#### 2.1. Concrete Individuals

A gufo:ConcreteIndividual, differently from a gufo:AbstractIndividual, is one that exists in space-time. Concrete individuals comprise objects (the Mount Everest, John, his car, the Brazilian 1988 Constitution), reified aspects of concrete individuals (John's height, his service agreement with Amazon, Inc.), events (the 1986 Mexico City Earthquake, the 2009 United Nations Climate Change Conference) and situations (the situation in which John weighs 80 kilograms, the situation in which Mary is a professor).

Together, objects and aspects form what we call endurants, as they are those concrete individuals that endure in time and may change qualitatively while keeping their identity. A gufo:Aspect is a characteristic or trait of a concrete individual that is itself conceived as an individual. Treating aspects as endurants (i.e., reifying aspects) allows us to consider the properties of aspects themselves, and track their change in time.

gUFO includes a number of data and object properties that can be used with concrete individuals. For example, temporal aspects of concrete individuals can be captured with the data properties gufo:hasBeginPointInXSDDate, gufo:hasBeginPointInXSDDateTimeStamp, gufo:hasEndPointInXSDDate and gufo:hasEndPointInXSDDateTimeStamp. In the case of objects (and aspects), these properties determine the time point when the object (or aspect) comes into existence or ceases to exist. In the case of events, these properties determine the time point when the event starts to take place or when it ends. In the case of situations, the properties determine the time point when the situation begins and ceases to hold. (Temporal instants may also be reified using time:Instant in which case the gufo:hasBeginPoint and gufo:hasEndPoint object properties are applicable, see [OWL-Time](https://www.w3.org/TR/owl-time/) for details concerning time:Instant, including support for Allen relations, temporal reference systems, temporal precision.)

For example, the 1985 Mexico City Earthquake started at 13:17:50 (UTC) on the 19th Sept. 1985 (scenario 1):

    :1985MexicoCityEarthquake rdf:type  gufo:Event ;
                       gufo:hasBeginPointInXSDDateTimeStamp "1985-09-19T13:17:50Z"^^xsd:dateTimeStamp .

By declaring Earthquake to be a sub-class of gufo:Event, the applicable object and data properties can be used with instances of earthquake (scenario 2):

    :Earthquake rdf:type owl:Class ;
                rdfs:subClassOf gufo:Event .

    :1985MexicoCityEarthquake rdf:type  :Earthquake ;
                            gufo:hasBeginPointInXSDDateTimeStamp "1985-09-19T13:17:50Z"^^xsd:dateTimeStamp .

gUFO also includes a number of part-whole relations for concrete individuals. See [gufo:isProperPartOf][] and its sub-properties.

<a name="objectsandparts"></a>

#### 2.2. Objects and their parts

Objects are further classified according to the way they are structured into parts, leading to the following subclasses: gufo:FunctionalComplex, gufo:Collection and gufo:Quantity.

A gufo:FunctionalComplex is a complex gufo:Object whose parts (components) play different roles in its composition, including most ordinary objects. For example, a person could be considered a gufo:FunctionalComplex with the various organs (heart, brain, lungs, etc.) playing different roles.

A gufo:Collection is a complex gufo:Object whose parts (the members of the collection) have a uniform structure (i.e., members are conceived as playing the same role in the collection). Examples include a deck of cards, a pile of bricks, a forest (conceived as a collection of trees), a group of people. Collections may have a variable or fixed membership (see subclasses gufo:VariableCollection and gufo:FixedCollection).

A gufo:Quantity is complex gufo:Object that is a maximally-connected portion of stuff. A gufo:Quantity has a fixed constitution, and thus, removing or adding a sub-quantity would result in a different quantity. Examples include the portion of wine in a wine tank, a lump of clay, the gold that constitutes a wedding ring.

The relations between a part and its whole are captured with the gufo:isObjectPropertPartOf property and its sub-properties, depending on the types of parts and complex objects involved:

> * isObjectProperPartOf
>     * isComponentOf - when the part is a component of a funcional complex
>     * isCollectionMemberOf - when the part is a member of a collection
>     * isSubCollectionOf - when the part is a collection containing a proper subset of all the member of another collection
>     * isSubQuantityOf - when the part and the whole are quantities

For example, John's brain is a component of John's:

    :John rdf:type :Person .

    :Brain rdf:type owl:Class ; 
            rdfs:subClassOf gufo:Object .

    :JohnsBrain rdf:type :Brain ;
            gufo:isComponentOf :John .

<a name="intrinsicaspects"></a>

#### 2.3. Intrinsic Aspects

The most straightforward way to describe intrinsic aspects of entities in a RDF/OWL setting is to employ data properties. For example, the following fragment defines a data property to represent the mass of a physical object in kilograms and declare a value for the Moon's mass:

    :hasMassInKilograms rdf:type owl:DatatypeProperty ;
                            rdfs:domain :PhysicalObject;
                            rdfs:range xsd:double .

    :Moon rdf:type :PhysicalObject ;
            :hasMassInKilograms "7.34767309E22"^^xsd:double .

While this is an adequate solution in many settings, some additional flexibility may be required, which can be obtained by treating an aspect as a concrete individual (instances of gufo:Aspect). This strategy is known as "reification".

Reified aspects in gUFO are further divided into intrinsic aspects (qualities and intrinsic modes) and extrinsic aspects (relators and extrinsic modes):

> * Endurant
>     * Aspect
>         * InstrinsicAspect
>             * Quality
>             * IntrinsicMode
>         * ExtrinsicAspect
>             * Relator
>             * ExtrinsicMode

A gufo:IntrinsicAspect depends on a single concrete individual in which it inheres. Examples include intrinsic physical aspects, such as the Moon's mass, Lassie's fur color; the fragility of John Lennon's glasses; mental dispositions, such as Bob's math skills, his belief that the number one is odd.

Intrinsic aspects are divided into qualities, in case the aspect is measurable by a certain value space (for example, Bob's weight, the height of the Statue of Liberty), and intrinsic modes, which are not given a direct value (for example, Bob's belief that the Eiffel Tower is in Paris, his capabilities).

<a name="basicqualities"></a>

#### 2.4. Qualities - Basic pattern

The turtle fragment below shows an example of definition of a quality type (mass) by specializing gufo:Quality:

    :Mass rdf:type owl:Class ;
                rdfs:subClassOf gufo:Quality .

As an intrinsic aspect, a gufo:Quality gufo:inheresIn a gufo:ConcreteIndividual. For example, the Moon's mass inheres in the Moon. Further, a quality may be given a value with the gufo:hasQualityValue data property. For example, consider the Moon's mass:

    :Moon rdf:type :PhysicalObject .

    :MoonsMass rdf:type :Mass ;
                    gufo:inheresIn :Moon
                    gufo:hasQualityValue "7.34767309E22"^^xsd:double .

A user may add that a mass must inhere in exactly one physical object:

    :Mass rdfs:subClassOf [ rdf:type owl:Restriction ;
                            owl:onProperty gufo:inheresIn ;
                            owl:qualifiedCardinality "1"^^xsd:nonNegativeInteger ;
                            owl:onClass :PhysicalObject
                           ] .

Further, a user may define specialized sub-properties of gufo:inheresIn in order to determine specific domain and range applicable to qualities of a certain type:

    :massOf rdf:type owl:ObjectProperty ;
            rdfs:subPropertyOf gufo:inheresIn ;
            rdfs:domain :Mass ;
            rdfs:range :PhysicalObject .

A user may also define sub-properties of gufo:hasQualityValue, for example with different ways to quantify a quality. Treating a quality (such as the Moon's mass) as a reified entity,  we can give it a value in different units (kilograms and in short tons):

    :massInKilograms rdf:type owl:DatatypeProperty ;
                            rdfs:subPropertyOf gufo:hasQualityValue ;
                            rdfs:domain :Mass ;
                            rdfs:range xsd:double .

    :massInShortTons rdf:type owl:DatatypeProperty ;
                            rdfs:subPropertyOf gufo:hasQualityValue ;
                            rdfs:domain :Mass ;
                            rdfs:range xsd:double .

    :MoonsMass rdf:type :Mass ;
                    :massOf :Moon ;
                    :massInKilograms "7.34767309E22"^^xsd:double ;
                    :massInShortTons "8.099423160000001E19"^^xsd:double .

(Other patterns for the representation of quality values are discussed below, including reification of quality values and situations employed to represent changes in qualities.)

<a name="advancedqualities"></a>

#### 2.5. Qualities - Advanced usage

In addition to the gufo:hasQualityValue data property, an object property called gufo:hasReifiedQualityValue is provided for those cases in which an instance of gufo:QualityValue is used instead of a literal to provide the value of a quality. Reifying a gufo:QualityValue may be useful in the case of enumerated values (for example, the various sizes of t-shirts), nominal qualities (for example, ethnicity or gender) or for quality values that are defined in terms of a multidimensional quality structure (such as color conceived in terms of red, green and blue components or hue, saturation and brightness).

In all these cases, a specialization of gufo:QualityValue is introduced. For example, consider the enumeration of shirt sizes:

    :ShirtSize rdf:type owl:Class ;
            rdfs:subClassOf gufo:QualityValue ;
            owl:equivalentClass [ rdf:type owl:Class ;
                                    owl:oneOf ( :S
                                                :M
                                                :L
                                                :XL
                                            )
                                ] .

    :S rdf:type :ShirtSize .
    :M rdf:type :ShirtSize .
    :L rdf:type :ShirtSize .
    :XL rdf:type :ShirtSize .

Consider color in a multidimensional RGB quality structure. Here, a corresponding sub-property of gufo:hasReifiedQualityValue ("hasColorValueInRGB") is also defined:

    :ColorValueInRGB rdf:type owl:Class ;
                    rdfs:subClassOf gufo:QualityValue .

    :hasColorValueInRGB rdf:type owl:ObjectProperty ;
                        rdfs:subPropertyOf gufo:hasReifiedQualityValue ;
                        rdfs:domain :Color ;
                        rdfs:range :ColorValueInRGB .

In the case of multidimensional quality values, it is recommended that subproperties of gufo:hasValueComponent are created to indicate values for particular dimensions, possibly identifying the datatype to be used. For example "hasRedValueComponent", "hasGreenValueComponent" and "hasBlueValueComponent" could be used as data properties specializing gufo:hasValueComponent with the xsd:nonNegativeInteger datatype.

    :hasRedValueComponent rdf:type owl:DatatypeProperty ;
                        rdfs:subPropertyOf gufo:hasValueComponent ;
                        rdfs:domain :ColorValueInRGB ;
                        rdfs:range xsd:nonNegativeInteger .

    :hasGreenValueComponent rdf:type owl:DatatypeProperty ;
                            rdfs:subPropertyOf gufo:hasValueComponent ;
                            rdfs:domain :ColorValueInRGB ;
                            rdfs:range xsd:nonNegativeInteger .

    :hasBlueValueComponent rdf:type owl:DatatypeProperty ;
                        rdfs:subPropertyOf gufo:hasValueComponent ;
                        rdfs:domain :ColorValueInRGB ;
                        rdfs:range xsd:nonNegativeInteger .

The following fragment determines the color of Yves Klein's "Blue Monochrome" painting made in 1961 (MoMA's object with number 618.1967) respecting the multidimensional scheme we have defined above:

    :YvesKleinBlueMonochromePainting rdf:type :PhysicalObject .

    :YvesKleinBlueMonochromePaintingColor rdf:type :Color ;
                        gufo:inheresIn :YvesKleinBlueMonochromePainting ;
                        :hasColorValueInRGB [ 
                            rdf:type :ColorValueInRGB ;
                            :hasRedValueComponent "0"^^xsd:nonNegativeInteger ;
                            :hasGreenValueComponent "47"^^xsd:nonNegativeInteger ;
                            :hasBlueValueComponent "167"^^xsd:nonNegativeInteger ] .

The example can be extended to capture the color in CMYK, HSB or other schemes.

<a name="intrinsicmodes"></a>

### 2.6. Intrinsic Modes

Intrinsic modes, unlike qualities, are not given values. The following fragment shows an example of a sub-class of gufo:IntrinsicMode and the corresponding sub-property of gufo:inheresIn establishing that a headache inheres in a person:

    :Headache rdf:type owl:Class ;
            rdfs:subClassOf gufo:IntrinsicMode .

    :headacheOf rdf:type owl:ObjectProperty ;
                rdfs:subPropertyOf gufo:inheresIn ;
                rdfs:domain :Headache ;
                rdfs:range :Person .

Since a gufo:IntrinsicMode is a gufo:ConcreteIndividual, we may track its temporal properties, as well as ascribe qualities (or other aspects) to it. For example, we may quantify the intensity of a headache with a quality and a [Verbal Rating Scale](https://doi.org/10.1177%2F0333102411434812)  (1 corresponding to "Mild pain", 2 corresponding to "Moderate pain", 3 corresponding to "Severe"):

    :johnsHeadache rdf:type :Headache ;
                :headacheOf :John;
                gufo:hasBeginPointInXSDDateTimeStamp "2019-11-19T14:14:50Z"^^xsd:dateTimeStamp .

    :HeadacheIntensity rdf:type owl:Class ;
                   rdfs:subClassOf gufo:Quality .

    :johnsHeadacheIntensity rdf:type :HeadacheIntensity ;
                gufo:inheresIn :johnsHeadache  ;
                gufo:hasQualityValue "2"^^xsd:nonNegativeInteger .

Further, by using situations, we can also track changes in an aspect over time, for example, to capture the evolution of a symptom, such as a headache and its intensity. See [situations](#situations) below.

<a name="extrinsicaspects"></a>

#### 2.7. Extrinsic Aspects

A gufo:ExtrinsicAspect is one that depends on one or more concrete individuals. Extrinsic (or "relational") aspects are reified relationships (instances of gufo:Relator), e.g., John and Mary's marriage, Mary's employment contract at Nasa.

A relator gufo:mediates concrete individuals. The following fragment shows an example of a sub-class of gufo:Relator and the corresponding sub-property of gufo:mediates establishing that persons are mediated through marriage:

    :Marriage rdf:type owl:Class ;
            rdfs:subClassOf gufo:Relator .

    :marriageInvolves rdf:type owl:ObjectProperty ;
                    rdfs:subPropertyOf gufo:mediates ;
                    rdfs:domain :Marriage ;
                    rdfs:range :Person .

The following fragment instantiates Marriage and establishes the related persons (John and Mary):

    :John rdf:type :Person .
    :Mary rdf:type :Person .

    :JohnMarysMarriage rdf:type :Marriage ;
                    :marriageInvolves :John ,
                                      :Mary .

A fuller application of the relator pattern can also make explicit the roles that are played in the scope of a relationship:

    :Employment rdf:type owl:Class ;
                rdfs:subClassOf gufo:Relator .

    :Employee rdf:type owl:Class ;
            rdfs:subClassOf :Person .

    :Organization rdf:type owl:Class ;
            rdfs:subClassOf gufo:Object .

    :Employer rdf:type owl:Class ;
            rdfs:subClassOf :Organization .

    :involvesEmployee rdf:type owl:ObjectProperty ;
                    rdfs:subPropertyOf gufo:mediates ;
                    rdfs:domain :Employment ;
                    rdfs:range :Employee .

    :involvesEmployer rdf:type owl:ObjectProperty ;
                    rdfs:subPropertyOf gufo:mediates ;
                    rdfs:domain :Employment ;
                    rdfs:range :Employer .

In the simpler cases, a user may alternatively choose to only declare that a marriage is a relator that involves persons. This pattern avoids the creation of subproperties of gufo:involves, but it prevents the explicit representation of roles:

    :Marriage rdfs:subClassOf [ rdf:type owl:Restriction ;
                                owl:onProperty gufo:mediates ;
                                owl:someValuesFrom :Person
                              ] .

Since a relator is a concrete individual, we may also track its temporal properties (begin and end date of employment) and ascribe other aspects to it (salary in the scope of the employment).

Note that, since OWL does not have dynamic classification, a person will be classified as an employee regardless of whether they have a current or past employment. Temporal properties of the employment will reflect whether employment is past.

Extrinsic aspects can also be reified one-sided relationships, e.g., John's admiration for Obama (which depends on Obama but does not characterize him). They can also be used to reveal parts of relators (instances of gufo:ExtrinsicMode), e.g., John's rights towards Amazon, Inc. (in the scope of a service agreement) and Amazon's reciprocal duties, Amazon's rights towards John, John's reciprocal duties:

    :AmazonInc rdf:type :Organization .

    :ServiceAgreement rdf:type owl:Class ;
            rdfs:subClassOf gufo:Relator .
 
    :JohnAmazonAgreement rdf:type :ServiceAgreement ;
                    :mediates :AmazonInc ,
                                :John .

    :JohnsRightToServiceProvisioning rdf:type gufo:ExtrinsicMode ;
                    gufo:inheresIn :John ;
                    gufo:externallyDependsOn :AmazonInc ;
                    gufo:isAspectProperPartOf :JohnAmazonAgreement .

    :AmazonsDutyToProvideService rdf:type gufo:ExtrinsicMode ;
                    gufo:inheresIn :AmazonInc ;
                    gufo:externallyDependsOn :John ;
                    gufo:isAspectProperPartOf :JohnAmazonAgreement .

    :AmazonsRightToPayment rdf:type gufo:ExtrinsicMode ;
                    gufo:inheresIn :AmazonInc ;
                    gufo:externallyDependsOn :John ;
                    gufo:isAspectProperPartOf :JohnAmazonAgreement .

    :JohnsDutyToPay rdf:type gufo:ExtrinsicMode ;
                    gufo:inheresIn :John ;
                    gufo:externallyDependsOn :AmazonInc ;
                    gufo:isAspectProperPartOf :JohnAmazonAgreement .    

<a name="events"></a>

#### 2.8. Events

A gufo:Event is a gufo:ConcreteIndividual that 'occurs' or 'happens' in time. They may be instantaneous or long-running. Events are those "things that happen to or are performed by" endurants ([Casati and Varzi, 2015][]).

Examples include actions and processes, such as a business meeting, a communicative act, a soccer match, a goal kick, the clicking of a mouse button; as well as natural occurrences such as an earthquake, the fall of the meteor that caused the extinction of the dinosaurs.

The following fragment shows examples of sub-classes of gufo:Event (NaturalDisaster, Earthquake, Tsunami, SoccerMatch), and an instance of SoccerMatch (WorldCup1970Final).

    :NaturalDisaster rdf:type owl:Class ;
                    rdfs:subClassOf gufo:Event .

    :Earthquake rdf:type owl:Class ;
                rdfs:subClassOf :NaturalDisaster ;
                owl:disjointWith :Tsunami .

    :Tsunami rdf:type owl:Class ;
            rdfs:subClassOf :NaturalDisaster .

    :SoccerMatch rdf:type owl:Class ;
                rdfs:subClassOf gufo:Event .

    :WorldCup1970Final rdf:type :SoccerMatch .

The implementation includes an object property to declare historical dependence between events. For example, the WorldCup1970Final depends historically on the two  semifinals:

    :WorldCup1970Final  gufo:historicallyDependsOn :BrazilUruguayWorldCup1970SemiFinal .
    :WorldCup1970Final  gufo:historicallyDependsOn :ItalyWestGermanyWorldCup1970SemiFinal .

The relations between objects and events may be captured with gufo:participatedIn, gufo:wasCreatedIn, gufo:wasTerminatedIn. Sub-properties of these object properties may be created to establish a particular domain and range. The following fragment establishes the participation of players in soccer matches, and defines that Pelé participated in the 1970 World Cup Final:

    :SoccerMatchPlayer rdf:type owl:Class ;
                    rdfs:subClassOf :Person .

    :participatedInMatch rdf:type owl:ObjectProperty ;
                        rdfs:subPropertyOf gufo:participatedIn ;
                        rdfs:domain :SoccerMatchPlayer ;
                        rdfs:range :SoccerMatch .

    :Pele rdf:type :Person ;
        :participatedInMatch :WorldCup1970Final .

Part-whole relations between events can be represented with the gufo:isEventProperPartOf object property:

    :WorldCup1970 rdf:type gufo:Event .

    :WorldCup1970Final rdf:type :SoccerMatch ;
                    gufo:isEventProperPartOf :WorldCup1970 .

See gufo:Participation for the cases in which we want to treat each participation as a part of an event with multiple participations.

An event can also be related to the endurants that are created or terminated in it. For example, John and Mary's marriage was brought into existence in their wedding ceremony:

    :JohnMarysMarriage rdf:type :Marriage ;
                    :marriageInvolves :John ,
                                        :Mary ;
                    gufo:wasCreatedIn :JohnMarysWedding.

    :JohnMarysWedding rdf:type gufo:Event 
                        gufo:hasBeginPointInXSDDate "2001-12-12"^^xsd:date .
                        gufo:hasEndPointInXSDDate "2001-12-12"^^xsd:date .

The Space Shuttle Challenger (OV-099) was tragically destroyed during the launch of its tenth flight on January 28, 1986:

    :Challenger rdf:type gufo:FunctionalComplex ;
            gufo:wasTerminatedIn :Challengers10thFlight .

    :Challengers10thLaunch rdf:type gufo:Event 
        gufo:hasBeginPointInXSDDate "1986-01-28"^^xsd:date ;
        gufo:hasEndPointInXSDDate "1986-01-28"^^xsd:date .

The gufo:manifestedIn property can be used to identify specific aspects that  manifest themselves in an event. For example, during the Challenger launch, a flaw in the seals of one of its rocket boosters led to catastrophic failure. Such a flaw can be considered an aspect of the seal, which was manifested in that event:

    :ChallengerRightBoosterSeal rdf:type gufo:FunctionalComplex ;
            gufo:isComponentOf :Challenger . 

    :ChallengerRightBoosterSealFlaw rdf:type gufo:IntrinsicMode ;
            gufo:inheresIn :ChallengerRightBoosterSeal ;
            gufo:manifestedIn :Challengers10thLaunch .

<a name="situations"></a>

#### 2.9. Situations 

Situations can be used to represent certain configurations of entities that can be comprehended as a whole. When that configuration is actual (present in reality), we say that a situation is a fact.

The various subclasses of gufo:Situation are used to represent "mutable" facts which obtain during some time and fail to obtain at other times. This includes the attribution of value to mutable qualities (such as a person's weight), the temporary instantiation of non-rigid types (e.g., as someone is a child at one point in time and a teenager later), the temporary participation in part-whole relations for replaceable parts (such as a car's tires), the temporary participation in constitution relations, and the temporary participation in mutable relations. Other subclasses may be created to capture domain-specific notions such as "HazardousSituation", "PersonHasFever".

We discuss here three of the various sub-classes of gufo:Situation (see [gufo:Situation][] and its sub-classes for other types of situations):

> * Individual
>     * AbstractIndividual
>     * ConcreteIndividual
>         * Situation
>             * QualityValueAttributionSituation
>             * TemporaryInstantiationSituation
>             * TemporaryParthoodSituation
>             * TemporaryConstitutionSituation
>             * TemporaryRelationshipSituation

A gufo:QualityValueAttributionSituation is used in a pattern when it is necessary to indicate the period of time in which the quality value attribution holds, and track changes in quality value. For example, consider tracking John's weight (technically, his mass) over the years. We declare various instances of gufo:QualityValueAttributionSituation and declare John to stand in these different situations with the gufo:standsInQualifiedAttribution object property:

    :JohnWeighs80Kgin2015 rdf:type gufo:QualityValueAttributionSituation ;
                        gufo:concernsQualityType :Mass ;
                        gufo:concernsQualityValue "80.0"^^xsd:double ;
                        gufo:hasBeginPointInXSDDate "2015-01-01"^^xsd:date ;
                        gufo:hasEndPointInXSDDate "2015-12-31"^^xsd:date .

    :JohnWeights70Kgin2018 rdf:type gufo:QualityValueAttributionSituation ;
                        gufo:concernsQualityType :Mass ;
                        gufo:concernsQualityValue "70.0"^^xsd:double ;
                        gufo:hasBeginPointInXSDDate "2018-01-01"^^xsd:date ;
                        gufo:hasEndPointInXSDDate "2018-12-31"^^xsd:date .

    :John gufo:standsInQualifiedAttribution :JohnWeighs80Kgin2015 ;
          gufo:standsInQualifiedAttribution :JohnWeights70Kgin2018 .

The gufo:concernsQualityValue data property is used to indicate a quality value attributed to the gufo:Endurant standing in the situation, and the gufo:concernsQualityType is used to identify the quality type (sub-class of gufo:Quality) whose value is attributed in the gufo:QualityValueAttributionSituation. (Use of a class such as Mass as an object in an object property requires punning. See [types](#types) below.)

Instances of gufo:TemporaryInstantiationSituation are used in a pattern when it is necessary to qualify the instantiation of non-rigid types with the period in time in which the instantiation holds. For example, consider subclasses of person representing life phases, such as Child, Adult, Senior:

    :Child rdf:type owl:Class ;
       rdfs:subClassOf :Person .

    :Adult rdf:type owl:Class ;
       rdfs:subClassOf :Person .

In this case, John was born in 1977 and is considered a child until 1995:

    :JohnWasAChildFrom1977to1995 rdf:type gufo:TemporaryInstantiationSituation ;
                                gufo:concernsNonRigidType :Child ;
                                gufo:hasBeginPointInXSDDate "1977-10-01"^^xsd:date ;
                                gufo:hasEndPointInXSDDate "1995-09-31"^^xsd:date .

    :JohnIsAdultFrom1995 rdf:type gufo:TemporaryInstantiationSituation ;
                                gufo:concernsNonRigidType :Adult ;
                                gufo:hasBeginPointInXSDDate "1995-10-01"^^xsd:date .

This is a reification of the instantiation (in a solution that is similar to the [qualified relation pattern](http://patterns.dataincubator.org/book/qualified-relation.html)).

Instances of gufo:TemporaryParthoodSituation are used in a pattern when it is necessary to qualify parthood and its change in time. In the following fragment, a heart transplant is tracked (from situations in which John and Paul have their original parts, to a situation in which there was a heart transplant from John to Paul).

    :JohnsHeart rdf:type :Heart ;
                gufo:standsInQualifiedParthood :JohnHasOriginalHeart .

    :PaulsHeart rdf:type :Heart ;
                gufo:standsInQualifiedParthood :PaulHasJohnsHeart ,
                                            :PaulHasOriginalHeart .

    :JohnHasOriginalHeart rdf:type gufo:TemporaryParthoodSituation ;
                        gufo:concernsTemporaryWhole :John ;
                        gufo:hasEndPointInXSDDate "2018-11-01"^^xsd:date .

    :PaulHasOriginalHeart rdf:type gufo:TemporaryParthoodSituation ;
                        gufo:concernsTemporaryWhole :Paul ;
                        gufo:hasEndPointInXSDDate "2018-11-01"^^xsd:date .

    :PaulHasJohnsHeart rdf:type gufo:TemporaryParthoodSituation ;
                        gufo:concernsTemporaryWhole :Paul ;
                        gufo:hasBeginPointInXSDDate "2018-11-01"^^xsd:date .

Instances of gufo:TemporaryConstitutionSituation are used in a pattern when it is necessary to qualify constitution and its change in time. In the following fragment, the quantity of marble that constitutes the Venus of Milo is tracked (from a situation in which it was constituted by its original quantity of marble, to a situation in which it is constituted by a smaller quantity of marble--after losing its arms, presumably in 1820).

    :VenusOfMilo rdf:type :Statue .

    :OriginalQuantityOfMarble rdf:type :AmountOfMarble ;
                gufo:standsInQualifiedConstitution :VenusHasArms .

    :ReducedQuantityOfMarble rdf:type :AmountOfMarble ;
                gufo:standsInQualifiedConstitution :VenusHasNoArms .

    :VenusHasArms rdf:type gufo:TemporaryConstitutionSituation ;
                        gufo:concernsConstitutedObject :VenusOfMilo ;
                        gufo:hasEndPointInXSDDate "1820-01-01"^^xsd:date .

    :VenusHasNoArms rdf:type gufo:TemporaryConstitutionSituation ;
                        gufo:concernsConstitutedObject :VenusOfMilo ;
                        gufo:hasBeginPointInXSDDate "1820-01-02"^^xsd:date .


Use gufo:TemporaryRelationshipSituation when it is necessary to qualify relations that change in time and determine the interval (or point in time) when the relationship applies to the involved entities. In the following fragment, John is declared heavier than Paul in a particular date.

    :heavierThan rdf:type owl:ObjectProperty ;
                rdfs:domain :PhysicalObject ;
                rdfs:range :PhysicalObject .

    :John rdf:type :PhysicalObject .
    :Paul rdf:type :PhysicalObject .

    :John :standsAsHeavierObject :JohnIsHeavier .           

    :JohnIsHeavier rdf:type gufo:TemporaryRelationshipSituation ;
                        gufo:concernsRelationshipType :heavierThan ;
                        :concernsLighterObject :Paul ;
                        gufo:hasBeginPointInXSDDate "2019-05-30"^^xsd:date ;
                        gufo:hasEndPointInXSDDate "2019-05-30"^^xsd:date.

    :standsAsHeavierObject rdfs:subPropertyOf gufo:standsInQualifiedRelationship .
    :concernsLighterObject rdfs:subPropertyOf gufo:concernsRelatedEndurant .            

For material relations (for example, Marriage, Enrollment, ServiceAgreement) prefer gufo:Relator to qualify relationships (see [Extrinsic Aspects](#extrinsicaspects)).

Situations can also be related to events through the gufo:broughtAbout and the gufo:contributedToTrigger properties. gufo:broughtAbout identifies a gufo:Situation that is brought about by a gufo:Event. For example, if the transplant had been represented explicitly, we could have established that it is the transplant that led to the new situations:

    :Transplant rdf:type owl:Class ;
       rdfs:subClassOf gufo:Event .

    :JohnToPaulHeartTransplant rdf:type :Transplant ;
        gufo:broughtAbout :PaulHasJohnsHeart .

We can also identify with gufo:contributedToTrigger those situations that contributed to triggering an event. For example, the fact that Host1234 was vulnerable contributed to its being involved in a security incident:

    :SecurityIncident rdf:type owl:Class ;
       rdfs:subClassOf gufo:Event .

    :WannaCryRansomwareAttackOnHost1234 rdf:type :SecurityIncident ;
                            gufo:hasBeginPointInXSDDate "2017-05-12"^^xsd:date ;
                            gufo:hasEndPointInXSDDate "2017-05-13"^^xsd:date ; .

    :ComputerSystem  rdf:type owl:Class ;
       rdfs:subClassOf gufo:Object .

    :Host1234 rdf:type :ComputerSystem ;
        gufo:participatedIn  :WannaCryRansomwareAttackOnHost1234 .

    :VulnerableSystem rdf:type owl:Class ;
            rdfs:subClassOf gufo:Object .

    :Host1234Vulnerable12May2017 rdf:type gufo:TemporaryInstantiationSituation ;
                                gufo:concernsNonRigidType :VulnerableSystem ;
                                gufo:hasBeginPointInXSDDate "2017-05-12"^^xsd:date ;
                                gufo:hasEndPointInXSDDate "2017-05-12"^^xsd:date ;
                                gufo:contributedToTrigger :WannaCryRansomwareAttackOnHost1234.

<a name="types"></a>

### 3. Taxonomy of Types

The taxonomy of types may be used to provide additional information about classes in UFO-based ontologies (usage scenario 3).

The taxonomy of types has the following overall structure:

> * Type
>     * AbstractIndividualType
>     * ConcreteIndividualType
>         * EndurantType
>             * Sortal
>                 * Kind
>                 * Phase
>                 * Role
>                 * SubKind
>             * NonSortal
>                 * Category
>                 * PhaseMixin
>                 * RoleMixin
>                 * Mixin
>         * EventType
>         * SituationType
>     * RelationshipType

The most abstract classes in this structure mostly reflect the taxonomy of individuals. For example, a gufo:AbstractIndividualType is a gufo:Type whose instances are abstract individuals (e.g., "NaturalNumber", "Set", "Proposition"), a gufo:EndurantType is a gufo:Type whose instances are objects and aspects (e.g., "Person", "Marriage", "Color"),  a gufo:EventType is a gufo:Type whose instances are events (e.g., "Earthquake", "MusicalPerformance"),  and so on.

<a name="enduranttypes"></a>

#### 3.1. Endurant types

The taxonomy of endurant types is more detailed, in order to qualify the ways in which an endurant type applies to their instances. For example, the following fragment declares Person to be a rigid sortal (a type that applies necessarily to its instances and provides them with identity criteria), Adult and Student to be anti-rigid sortals (types that apply contingently to their instances and carry a principle of identify provided by a kind). Since Adult is a phase, it applies to its instances in virtue of some intrinsic aspects. Since Student is a role, it applies to its instances in virtue of some extrinsic aspects.  

    :Person rdf:type gufo:Kind .

    :Adult rdf:type gufo:Phase ;
        rdfs:subClassOf :Person .

    :Student rdf:type gufo:Role ;
        rdfs:subClassOf :Person .

These declarations allow tools to detect representational mistakes, e.g., it is invalid for a gufo:Kind to be a sub-class of a gufo:Phase or gufo:Role; for an object to be an instance of more than one gufo:Kind, for a gufo:Kind to specializes any other sortal that specializes another gufo:Kind, etc.

See [Guizzardi, 2005][] and [Guizzardi et al., 2018][] for details concerning the taxonomy of endurant types.

This representation strategy employs OWL 2 punning, when a class is also treated as an instance of another class (in this case, `:Person rdf:type gufo:Kind` and, as defined in gUFO, `gufo:Kind rdf:type owl:Class`).

<a name="relationshiptypes"></a>

#### 3.2. Relationship types

The gufo:RelationshipType class and its subclasses are introduced to qualify the ways in which an object property relates entities in UFO-based ontologies. For example, object properties such as "marriedWith" and "enrolledIn" can  be declared to be instances of gufo:MaterialRelationshipType, which means we can identify the type of extrinsic aspect from which the material relationship type is derived (see [gufo:isDerivedFrom](#isDerivedFrom)). For instance, "marriedWith" can be derived from the "Marriage" relator type:

    :marriedWith rdf:type owl:ObjectProperty ,
                    gufo:MaterialRelationshipType;
             rdfs:domain :Person ;
             rdfs:range :Person ;
             gufo:isDerivedFrom :Marriage .

See [gufo:RelationshipType](#RelationshipType) for other sub-classes, including gufo:ComparativeRelationshipType, which can be reduced to intrinsic aspects of related entities.

<a name="highordertypes"></a>

#### 3.3. High-order types

In usage scenario 4, a UFO-based ontology specializes gUFO classes in the taxonomy of types, for example, in order to represent roles that persons play: `:PersonRole rdfs:subClassOf gufo:Role`.

In these cases, a user may want to establish explicitly the relation between "PersonRole" (the second-order type) and "Person" (the first-order type). For this purpose, the gufo:categorizes property is provided. It identifies a gufo:Type whose instances may be classified by instances of the categorizing higher-order type.

The categorized type is termed the "base type" in the "powertype pattern" see ([Carvalho et al., 2017][]), the higher-order type is often called the "powertype".  

    :PersonRole gufo:categorizes :Person ;
        rdfs:subClassOf gufo:Role .

    :Student rdf:type :PersonRole ;
            rdfs:subClassOf :Person .
    :Professor rdf:type :PersonRole ;
            rdfs:subClassOf :Person .

OWL 2 punning is used to capture the two facets of "Student" and "Professor" in this example: (i) as instances of "PersonRole", and (ii) as subclasses of "Person".

In another example, "ShipType" gufo:categorizes "Ship" and is a subclass of "gufo:SubKind". Instances of "ShipType" such as "Supercarrier" and "CargoShip" should be declared subclasses of "Ship".

    :ShipType gufo:categorizes :Ship ;
        rdfs:subClassOf gufo:SubKind .

    :Supercarrier rdf:type :ShipType ;
            rdfs:subClassOf :Ship .
    :CargoShip rdf:type :ShipType ;
            rdfs:subClassOf :Ship .

gufo:categorizes is the general (unspecific) form of categorization. The sub-property gufo:partitions provides a more specific form, in which instances of the categorized type are classified by *exactly one* instance of the higher-order type.

For example, "AnimalSpecies" gufo:partitions "Animal". Instances of "AnimalSpecies" such as "Lion", "Hiena" must be disjoint subclasses of "Animal". OWL 2 punning should be used to capture the two facets of "Lion" and "Hiena" in this example: (i) as instances of "AnimalSpecies", and (ii) as  subclasses of "Animal".

    :AnimalSpecies gufo:partitions :Animal .

    :Hiena rdf:type :AnimalSpecies ;
            rdfs:subClassOf :Animal .
    :Lion rdf:type :AnimalSpecies ;
            rdfs:subClassOf :Animal ;
            owl:disjointWith :Hiena .

    :Cecil rdf:type :Lion .

Note that the partitioned type (in the example "Animal") may or may not be declared to be a disjoint union of the explicitly enumerated subclasses (such as "Lion", "Hiena"). This is because other instances of the higher-order type ("AnimalSpecies") may exist that are not explicitly enumerated in the ontology.

The partitioned type is termed the "base type" in the "powertype pattern" see ([Carvalho et al., 2017][]), the higher-order type is often called the "powertype".  

For further details and formalization of "partitioning", see ([Carvalho et al., 2017][]) which combines UFO with MLT (a multi-level modeling theory).  

[gufo:Individual]: #Individual
[individual]: #Individual
[individuals]: #Individual
[gufo:Situation]: #Situation
[gufo:isProperPartOf]: #isProperPartOf
[gufo:RelationshipType]: #RelationshipType
[Casati and Varzi, 2015]: https://plato.stanford.edu/archives/win2015/entries/events/
[Guizzardi et al., 2018]: https://doi.org/10.1007/978-3-030-00847-5_12
[Guizzardi, 2005]: https://research.utwente.nl/en/publications/ontological-foundations-for-structural-conceptual-models
[Carvalho et al., 2017]: <http://dx.doi.org/10.1016/j.datak.2017.03.002>

