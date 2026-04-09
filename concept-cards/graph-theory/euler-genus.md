---
concept: Euler Genus
slug: euler-genus
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Appendix B - Surfaces"
chapter_number: null
pdf_page: 374
section: null
extraction_confidence: high
aliases:
  - "epsilon(S)"
prerequisites:
  - euler-characteristic
extends:
  - euler-characteristic
related:
  - genus
  - handle
  - crosscap
contrasts_with:
  - genus
answers_questions:
  - "What is the Euler genus?"
  - "How is the Euler genus computed?"
---

# Quick Definition
The Euler genus epsilon(S) = 2 - chi(S) is a non-negative integer invariant of surfaces. It increases by 2 for each handle and by 1 for each crosscap added to the sphere.

# Core Definition
"This invariant chi of S is its Euler characteristic. For computational simplicity we usually work instead with the derived invariant epsilon(S) := 2 - chi(S), the Euler genus of S, because chi is negative for most surfaces but epsilon takes its values in N" (Diestel, p. 363).

# Prerequisites
- **Euler characteristic** -- epsilon = 2 - chi

# Key Properties
1. epsilon(S^2) = 0 (sphere)
2. Adding a handle raises epsilon by 2 (Lemma B.3(i))
3. Adding a crosscap raises epsilon by 1 (Lemma B.3(ii))
4. epsilon >= 0 for all surfaces
5. Cutting along a non-separating one-sided circle reduces epsilon by 1 (Lemma B.4(i))
6. Cutting along a non-separating two-sided circle reduces epsilon by 2 (Lemma B.4(ii))
7. For separating circles: epsilon(S) = epsilon(S') + epsilon(S'') (Lemma B.5)

# Context & Application
The Euler genus is preferred over the Euler characteristic for computational reasons (it's non-negative). It enables induction on surface complexity: every non-sphere surface contains a non-separating circle, and cutting along it reduces the Euler genus.

# Relationships
## Builds Upon
- **Euler characteristic**

## Related
- **Handle** -- Adds 2 to epsilon
- **Crosscap** -- Adds 1 to epsilon
- **Genus** -- For orientable surfaces, epsilon = 2g where g is the genus

# Contrasts With
- **Genus** -- The orientable genus g counts handles only; epsilon = 2g for orientable surfaces, epsilon = number of crosscaps for non-orientable

# Source Reference
Appendix B, page 363. Lemmas B.3, B.4, B.5.

# Verification Notes
- Definition from p. 363
- Confidence: HIGH -- explicit definition with supporting lemmas
