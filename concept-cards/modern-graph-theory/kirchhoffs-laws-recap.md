---
concept: "Kirchhoff's Laws Recap"
slug: kirchhoffs-laws-recap
category: electrical-networks
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 297
section: "IX.1 Electrical Networks Revisited"
extraction_confidence: high
aliases:
  - "Ohm's law"
  - "KPL"
  - "KCL"
prerequisites: []
extends: []
related:
  - energy-in-electrical-network
  - thomsons-principle
  - dirichlets-principle
contrasts_with: []
answers_questions:
  - "What must I know before understanding random walks on graphs?"
---

# Quick Definition
The three laws governing electrical networks: Ohm's law ($w_e = p_e/r_e$), Kirchhoff's potential law (KPL: potential differences around cycles sum to 0), and Kirchhoff's current law (KCL: total current into each non-outlet vertex is 0).

# Core Definition
Bollobás recapitulates from Chapter II (p. 297): OL: $w_e = p_e/r_e$. KPL: "the sum of potential differences around any cycle is 0." KCL: "the total current into a vertex is 0." By Kirchhoff's theorem (II.1), these laws uniquely determine the current distribution for given sources and sinks.

# Prerequisites
Foundational -- recapitulated from Chapter II.

# Key Properties
1. OL, KPL, KCL together uniquely determine currents
2. KPL $\Leftrightarrow$ existence of absolute potentials
3. KCL $\Leftrightarrow$ conservation of current at non-outlet vertices
4. The energy minimization approach (Thomson/Dirichlet) uses only some of these laws

# Context & Application
Chapter IX revisits these laws to develop the energy optimization viewpoint, which is "much better" (p. 298) than the static approach for proving the monotonicity principle and connecting to random walks.

# Relationships
## Related
- **energy-in-electrical-network**, **thomsons-principle**, **dirichlets-principle**

# Source Reference
Chapter IX, Section IX.1, pages 297-298. Original in Chapter II.

# Verification Notes
- Definition source: Recap from p. 297
- Confidence rationale: Explicit recapitulation
- Uncertainties: None
- Cross-reference status: Verified against Ch II
