---
concept: Stereographic Projection
slug: stereographic-projection
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.2 Interlude: Spheres"
extraction_confidence: high
aliases: []
prerequisites: [n-sphere]
extends: []
related: [special-unitary-group-su2]
contrasts_with: []
answers_questions: ["What is stereographic projection?"]
---
# Quick Definition
Stereographic projection maps the n-sphere minus the north pole bijectively to n-dimensional space R^n. It provides a way to build spheres from flat space and gives coordinates on spheres.
# Core Definition
Stereographic projection pi: S^n -> R^n is defined by projecting from the north pole p = (1, 0, ..., 0) through each point x on the sphere to the hyperplane {x_0 = 0}. The formula is pi(x) = (x_1/(1-x_0), ..., x_n/(1-x_0)) (Artin, (9.2.3), p. 267). The projection is bijective at all points except p, which is "sent to infinity."
# Prerequisites
- **n-sphere** — The domain of stereographic projection
# Key Properties
1. Bijective from S^n minus north pole to R^n
2. Formula: pi(x) = (x_1/(1-x_0), ..., x_n/(1-x_0))
3. The sphere can be built topologically as R^n plus one point
4. Maps the lower hemisphere to the unit disk, upper hemisphere to the exterior
5. Is the identity on the equator
# Context & Application
Stereographic projection is used to give coordinates on spheres and to understand the topology of SU_2 (homeomorphic to S^3). It provides the key topological constructions used to describe the 3-sphere.
# Examples
**Example 1** (p. 266): For S^2: pi(x_0, x_1, x_2) = (x_1/(1-x_0), x_2/(1-x_0)).
# Relationships
## Builds Upon
- **n-sphere** — The domain
## Related
- **Special unitary group SU_2** — SU_2 = S^3, and stereographic projection gives coordinates
# Source Reference
Chapter 9: Linear Groups, Section 9.2, pages 266-268.
# Verification Notes
- Definition source: Direct from (9.2.2) and (9.2.3)
- Confidence rationale: Explicitly defined with formula
- Uncertainties: None
- Cross-reference status: Verified
