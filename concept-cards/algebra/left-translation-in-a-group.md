---
concept: Left Translation in a Group
slug: left-translation-in-a-group
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.7 Translation in a Group"
extraction_confidence: high
aliases: ["left multiplication", "translation in a group"]
prerequisites: [classical-groups]
extends: []
related: [manifold-linear-group]
contrasts_with: []
answers_questions: ["What is left translation in a matrix group?"]
---
# Quick Definition
Left translation by P in a matrix group G is the map m_P: G -> G defined by X -> PX. It is a homeomorphism from G to itself, giving G a homogeneity property: the group "looks the same" at every point.
# Core Definition
Left multiplication by P is a bijective map m_P: G -> G, X -> PX, with inverse m_{P^{-1}} (Artin, (9.7.1), p. 288). Both m_P and its inverse are continuous, so m_P is a homeomorphism. This gives groups a homogeneity property: the group looks the same at P as it does at I, for any P.
# Prerequisites
- **Classical groups** — Translation is studied in matrix groups
# Key Properties
1. m_P is a homeomorphism (not a homomorphism)
2. Carries the identity I to P
3. The group looks the same at every point (homogeneity)
4. Used to prove classical groups are manifolds (local structure at I extends to all points)
5. Used to prove path-connected groups with open subgroups are trivial (Proposition 9.7.9)
# Context & Application
Homogeneity via translation is the key geometric property of groups. It is used to extend local analysis (near the identity) to global results, and to prove simplicity results for SU_2 and SO_3.
# Examples
**Example 1** (p. 288): In SO_2, left multiplication rotates the circle.
**Example 2** (p. 289): In the group of invertible diagonal 2x2 matrices, multiplication by diag(2,1) stretches the group continuously.
# Relationships
## Enables
- **Manifold structure** — Local analysis at I extends to all points via translation
# Source Reference
Chapter 9: Linear Groups, Section 9.7, pages 288-289.
# Verification Notes
- Definition source: Direct from (9.7.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
