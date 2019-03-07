## Abstract

   Biomedical ontologies help specify how to integrate data from various sources and organize data and information in a way that computers can use for large-scale analysis. Opioid use disorder is a growing public health problem. Its impact on public health is so profound that mortality from opioid use disorder drove a decline in the average US life expectancy last year. Treatment for opioid use disorder involves therapy, medication, and social support. An ontology that organizes the opioid use disorder research could improve the treatment of patients suffering from opioid use disorder by identifying the evidence for certain treatments in specific patients. Here, building towards an ontology of the research on opioid use disorder treatment, we provide an logically consistent representation of the terms _substance use_, _substance misuse_, and _substance abuse_. This representation is compatible with Basic Formal Ontology, the Ontology of Mental Function, and the Ontology of Mental Disease. 

## Background

#### Terminology Used in the Field 
The Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition defines substance use disorders as:

 > Patterns of symptoms resulting from the use of a substance that you continue to take, despite experiencing problems as a result.
 
 The DSM-V distinguishes substance use disorders, from substance-induced disorders, which are direct physical manifestations of substance use, for example intoxication, withdrawal, or temporary psychosis. 

The term _substance use_ is preferred over _substance abuse_ or _substance misuse_, especially in materials that guide how healthcare providers interact with patients who may have an unproductive reaction to terms like _abuse_ or _misuse_. 

#### Current Ontological Representation
The Ontology of Mental Disease represents addiction and substance-related disorder as occurents [(Hastings et al., 2010)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3017014/). An occurent is an entity that has temporal parts, whose existence happens, unfolds, or develops through time [(citation)](http://purl.obolibrary.org/obo/bfo.owl). Figure 1 shows a selected view of the hierarchy. 

    occurent
    |---process
        |----disease course
            |---mental disease course
                |---mental disorder
                    |--- addiction disorder
     
    Figure 1. View of OMD Hierarchy that includes addiction disorder as a subtype of occurrent. 
    
OMD does not use the term _substance use disorder_. It, instead, uses the term _substance-related disorder_. This is in keeping with the DSM-IV-TR, which was the current terminological standard when OMD was published. 

**Proposed Changes** 

We propose to unify the terms _substance dependence_ and _substance-related disorder_ under the term _substance use disorder_. We propose the following definition of a _substance use disorder_. 

(Could unify _substance dependence_ and _process addiction_ under 

> A substance use disorder is a mental disorder that involves 

We propose to replace the term _addiction disorder_ with 

We propose to replace _substance related disorder_ with _substance use disorder_. OMD defines _substance-related disorder_ as follows.

>A disease of mental health involving the abuse or dependence on a substance that is ingested in order to produce a high, alter one's senses, or otherwise affect functioning.

**A normative theory of substance use** We wish to represent that the pathological component of a substance user disorder arises from the pattern of use. 

---

[Draft Notes]

[link to ontology](./mln/data/tracking-adding-entries.md) 
Need to answer how these relate to addiction 
