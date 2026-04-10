---
concept: Uniqueness Characterization of the Tutte Polynomial
slug: tutte-polynomial-uniqueness-characterization
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 344
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - deletion-contraction
  - multiplicativity-of-tutte-polynomial
extends: []
related:
  - universal-polynomial-of-graphs
contrasts_with: []
answers_questions:
  - "What is the Tutte polynomial?"
---

# Quick Definition
The Tutte polynomial $T$ is the unique function on graphs such that: (i) if $G$ has $b$ bridges, $\ell$ loops and no other edges then $T_G = x^b y^\ell$; (ii) adding bridges/loops multiplies by $x$/$y$; (iii) for some non-bridge non-loop edge $e$: $T_G = T_{G-e} + T_{G/e}$.

# Core Definition
$T$ is "the unique function on graphs such that: (i) if $G$ has $b$ bridges, $\ell$ loops and no other edges then $T_G = x^b y^\ell$, (ii) if $G$ is obtained from $H$ by adding $b$ bridges and $\ell$ loops then $T_G = x^b y^\ell T_H$, (iii) if $G$ has no bridges or loops then the third recursion formula holds for some edge $e$" (Bollobás, p. 344).

# Prerequisites
- **Tutte polynomial**, **deletion-contraction**, **multiplicativity-of-tutte-polynomial**

# Key Properties
1. Three conditions uniquely determine $T$
2. Alternatively: multiplicativity + recursion + $T(K_2) = x$, $T(L) = y$
3. Provides a verification tool: to show a function equals $T_G$, check these conditions

# Context & Application
This characterization is used throughout Chapter X to prove that various quantities (chromatic polynomial, flow polynomial, partition functions) are evaluations of the Tutte polynomial: verify the recursion and boundary conditions.

# Relationships
## Builds Upon
- **tutte-polynomial**, **deletion-contraction**, **multiplicativity-of-tutte-polynomial**

## Related
- **universal-polynomial-of-graphs** — Analogous characterization with more parameters

# Source Reference
Chapter X, Section X.1, page 344.

# Verification Notes
- Definition source: Direct from p. 344
- Confidence rationale: Explicit characterization
- Uncertainties: None
- Cross-reference status: Verified
