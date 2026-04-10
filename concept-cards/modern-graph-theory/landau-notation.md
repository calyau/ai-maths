---
concept: Landau Notation in Extremal Graph Theory
slug: landau-notation
category: extremal-graph-theory
subcategory: notation
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "O notation"
  - "o notation"
  - "asymptotic notation"
prerequisites: []
extends: []
related:
  - extremal-function
  - erdos-stone-theorem
contrasts_with: []
answers_questions:
  - "What do O and o notation mean in extremal graph theory?"
---

# Quick Definition
$g = O(f)$ if $g/f$ is bounded as $n \to \infty$; $g = o(f)$ if $g/f \to 0$ as $n \to \infty$. In particular, $o(1)$ denotes a function tending to 0.

# Core Definition
We use Landau's notation: $g = O(f)$ if $g/f$ is bounded as $n \to \infty$, and $g = o(f)$ if $g/f \to 0$ as $n \to \infty$. In particular, $o(1)$ denotes a function tending to 0 as $n \to \infty$ (Bollobás, p. 117).

# Prerequisites
This is a foundational notation with no prerequisites.

# Key Properties
1. Used throughout extremal graph theory for asymptotic results
2. $t_r(n) = (1-1/r+o(1))\binom{n}{2}$
3. $ex(n;F) = (1-1/r)\binom{n}{2} + o(n^2)$ for $\chi(F) = r+1$

# Context & Application
Asymptotic notation enables stating results that hold "for $n$ large enough" in a compact form.

# Examples
**Example** (p. 117): $t_r(n) = (1-1/r+o(1))\binom{n}{2}$ for fixed $r$ and $n \to \infty$.

# Relationships
## Related
- **extremal-function** — Often expressed asymptotically
- **erdos-stone-theorem** — Key asymptotic result

# Source Reference
Chapter IV, Section IV.2, page 117.

# Verification Notes
- Definition source: Direct from p. 117
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
