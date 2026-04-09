---
concept: "Gallai's Theorem"
slug: gallais-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 54
section: "2.3 Packing and covering"
extraction_confidence: medium
aliases:
  - "Gallai identity"
  - "Gallai's identities"
prerequisites:
  - vertex-cover
  - independent-set
  - matching
  - edge-cover
extends: []
related:
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "How are vertex covers related to independent sets?"
  - "How are matchings related to edge covers?"
---

# Quick Definition
Gallai's theorem establishes two identities: (1) alpha(G) + tau(G) = |V|, where alpha is the independence number and tau is the minimum vertex cover; (2) alpha'(G) + beta'(G) = |V|, where alpha' is the maximum matching and beta' is the minimum edge cover.

# Core Definition
**Gallai's identities** relate the four fundamental parameters: (1) The independence number alpha(G) plus the minimum vertex cover number tau(G) equals |V(G)|. (2) The maximum matching number alpha'(G) plus the minimum edge cover number beta'(G) equals |V(G)| (for graphs without isolated vertices).

# Prerequisites
- **Vertex cover** — tau(G) = minimum vertex cover size
- **Independent set** — alpha(G) = maximum independent set size
- **Matching** — alpha'(G) = maximum matching size
- **Edge cover** — beta'(G) = minimum edge cover size

# Key Properties
1. alpha(G) + tau(G) = |V| (complement relationship: V \ cover = independent set)
2. alpha'(G) + beta'(G) = |V| (for graphs with no isolated vertices)
3. The first identity is immediate from the definitions
4. The second follows because extending a maximum matching by one edge per unmatched vertex gives an edge cover

# Construction / Recognition
## Deriving the Identities
1. For alpha + tau = |V|: if U is a minimum vertex cover, then V \ U is a maximum independent set
2. For alpha' + beta' = |V|: extend a maximum matching M by adding one edge per unmatched vertex to get an edge cover of size |M| + (|V| - 2|M|) = |V| - |M|

# Context & Application
Gallai's identities tie together the four fundamental covering/packing parameters. Combined with Konig's theorem (tau = alpha' in bipartite graphs), they yield additional equalities for bipartite graphs.

# Examples
**Example**: In K4, alpha = 1, tau = 3, |V| = 4: 1 + 3 = 4. alpha' = 2, beta' = 2: 2 + 2 = 4.

# Relationships
## Builds Upon
- **Vertex cover**, **independent set**, **matching**, **edge cover**

## Related
- **Konig's theorem** — combined with Gallai gives alpha = |V| - alpha' in bipartite graphs

# Common Errors
- **Error**: Applying the edge cover identity to graphs with isolated vertices
  **Correction**: alpha' + beta' = |V| requires no isolated vertices (isolated vertices have no incident edges)

# Common Confusions
- **Confusion**: Thinking Gallai's theorem is a single identity
  **Clarification**: There are two identities, one for vertex parameters and one for edge parameters

# Source Reference
Chapter 2, Section 2.3 context. Standard results in matching theory.

# Verification Notes
- Identities standard in the covering/packing framework of Section 2.3
- Confidence: MEDIUM — implicit in the section; not stated as a single named theorem in the text
