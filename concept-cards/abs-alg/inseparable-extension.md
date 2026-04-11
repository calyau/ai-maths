---
concept: Inseparable Extension
slug: inseparable-extension
category: field-theory
subcategory: separability
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 547
section: "13.5 Separable and Inseparable Extensions"
extraction_confidence: high
aliases:
  - "inseparable polynomial"
  - "purely inseparable extension"
prerequisites:
  - separable-extension
extends: []
related:
  - perfect-field
contrasts_with:
  - separable-extension
answers_questions:
  - "What is an inseparable extension?"
---

# Quick Definition
An irreducible polynomial is inseparable if it has repeated roots (only possible in characteristic p). An element $\alpha$ is inseparable over F if its minimal polynomial is inseparable. An extension is purely inseparable if every element has minimal polynomial of the form $x^{p^k} - a$.

# Core Definition
An irreducible polynomial $f(x) \in F[x]$ is inseparable iff $f'(x) = 0$, which can only happen in characteristic $p > 0$ when $f(x) = g(x^p)$ for some polynomial g. An element is inseparable over F if its minimal polynomial is inseparable. An algebraic extension K/F is purely inseparable if every element $\alpha \in K$ satisfies $\alpha^{p^k} \in F$ for some $k \geq 0$ (Dummit & Foote, pp. 547-554).

# Prerequisites
- **separable-extension** — Inseparable is the negation of separable

# Key Properties
1. Inseparability only occurs in characteristic p > 0
2. An irreducible polynomial is inseparable iff it is a polynomial in $x^p$
3. Over perfect fields, no inseparable polynomials exist
4. Any algebraic extension decomposes: $K/K_s/F$ where $K_s/F$ is separable and $K/K_s$ is purely inseparable

# Relationships
## Builds Upon
- **separable-extension**

## Related
- **perfect-field** — Perfect fields have no inseparable extensions

## Contrasts With
- **separable-extension** — No repeated roots

# Source Reference
Chapter 13, Section 13.5, pp. 547-554.

# Verification Notes
- Confidence: HIGH — explicit definitions
