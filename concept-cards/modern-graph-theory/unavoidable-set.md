---
concept: Unavoidable Set of Configurations
slug: unavoidable-set
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
  - euler-formula-for-planar-graphs
extends: []
related:
  - reducible-configuration
  - discharging-method
contrasts_with: []
answers_questions:
  - "What is an unavoidable set of configurations?"
---

# Quick Definition
A set of configurations is unavoidable if every plane graph must contain at least one configuration from the set. Euler's formula and discharging arguments show unavoidability.

# Core Definition
A set of configurations is **unavoidable** if every plane graph contains at least one configuration belonging to the set. To prove the four-colour theorem, one must find an unavoidable set of reducible configurations. Unavoidability is proved using Euler's formula via discharging: assign charge 6 − k to each vertex of degree k, giving total charge 12, then redistribute charges according to discharging rules until a configuration becomes visible (Bollobás, pp. 166–167).

# Prerequisites
- **Four colour theorem** — unavoidability is part of its proof
- **Euler's formula for planar graphs** — the source of the total charge

# Key Properties
1. For the five-colour theorem: vertices of degree ≤ 5 form an unavoidable set
2. For the four-colour theorem: Appel-Haken used 300+ discharging rules
3. Robertson et al. used 32 discharging rules

# Relationships
## Related
- **Reducible configuration** — the companion concept
- **Discharging method** — the technique for proving unavoidability

# Source Reference
Chapter V: Colouring, Section V.3, pages 166–167.

# Verification Notes
- Definition source: Direct from pp. 166–167
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
