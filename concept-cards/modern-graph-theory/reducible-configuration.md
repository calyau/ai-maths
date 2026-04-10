---
concept: Reducible Configuration
slug: reducible-configuration
category: planar-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 166
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases: []
prerequisites:
  - four-colour-theorem
  - kempe-chain
extends: []
related:
  - unavoidable-set
  - discharging-method
contrasts_with: []
answers_questions:
  - "What is a reducible configuration in the four-colour theorem proof?"
---

# Quick Definition
A configuration is reducible if no minimal 5-chromatic plane graph can contain it. Finding reducible configurations is one of the two key tasks in proving the four-colour theorem.

# Core Definition
A **configuration** is a connected cluster of vertices of a plane graph together with the degrees of the vertices. A configuration is **reducible** if no minimal 5-chromatic plane graph can contain it. Reducibility is shown by replacing the cluster with a smaller one, 4-colouring the smaller graph, and using Kempe chains to pull back the colouring (Bollobás, pp. 166–167).

# Prerequisites
- **Four colour theorem** — reducibility is used in its proof
- **Kempe chain** — technique for showing reducibility

# Key Properties
1. A single vertex of degree ≤ 5 is a reducible configuration for the five-colour theorem
2. Appel-Haken needed over 1900 reducible configurations
3. Robertson et al. reduced to 633 reducible configurations
4. Checking reducibility involves Kempe chain analysis and computer verification

# Examples
**Example** (p. 167, Figure V.8): Three reducible configurations are shown.

# Relationships
## Related
- **Unavoidable set** — complementary concept; together they prove the theorem
- **Discharging method** — used to show unavoidability

# Source Reference
Chapter V: Colouring, Section V.3, pages 166–167.

# Verification Notes
- Definition source: Direct from pp. 166–167
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
