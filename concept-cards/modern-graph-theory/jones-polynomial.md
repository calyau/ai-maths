---
concept: Jones Polynomial
slug: jones-polynomial
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 371
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "V_L(t)"
prerequisites:
  - kauffman-bracket
  - writhe
extends: []
related:
  - one-variable-kauffman-polynomial
  - tutte-polynomial-and-jones-polynomial
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The Jones polynomial $V_L(t) \in \mathbb{Z}[t^{1/2}, t^{-1/2}]$ is an ambient isotopy invariant of oriented links, defined by $V_{\bigcirc} = 1$ and the skein relation $t^{-1}V_{\nearrow} - tV_{\searrow} = (\sqrt{t} - 1/\sqrt{t})V_{\asymp}$.

# Core Definition
The Jones polynomial $V_L(t)$ was "constructed by Vaughan Jones in 1985" (p. 371). It is the unique Laurent polynomial in $\mathbb{Z}[t^{1/2}, t^{-1/2}]$ satisfying $V_{\bigcirc} = 1$ and the skein relation (equation (9)). Theorem 19 (p. 372): $V_L(t) = f[L](t^{-1/4})$ where $f[L] = (-A)^{-3w(L)} \langle L \rangle(A)$.

# Prerequisites
- **Kauffman bracket** — $V_L(t)$ is obtained from the bracket by substitution
- **Writhe** — Appears in the normalization factor

# Key Properties
1. Ambient isotopy invariant for oriented links
2. $V_L(t) = f[L](t^{-1/4})$
3. Satisfies the skein relation (equation (9))
4. Can distinguish many knots and links
5. For alternating links: expressible via the Tutte polynomial (Theorem 21)
6. Can prove certain knots are knotted (not equivalent to unknot)

# Context & Application
"Jones started a revolution in knot theory by introducing a new polynomial invariant, which later was shown to be closely related to the Tutte polynomial" (p. 363). The Jones polynomial can distinguish knots that classical invariants cannot, though it is not a complete invariant (Exercise 41: knots $8_8$ and $10_{129}$ have equal Jones polynomials).

# Examples
**Example** (p. 371): The one-variable Kauffman polynomial of the right-handed trefoil is $-A^{-16} + A^{-12} + A^{-4}$, giving a Jones polynomial that proves the trefoil is knotted and not amphicheiral.

# Relationships
## Builds Upon
- **kauffman-bracket**, **writhe**

## Related
- **tutte-polynomial-and-jones-polynomial** — For alternating links, Jones = evaluation of Tutte
- **one-variable-kauffman-polynomial** — $V_L(t) = f[L](t^{-1/4})$

# Source Reference
Chapter X, Section X.6, Theorem 19, pages 371-372.

# Verification Notes
- Definition source: Direct from Theorem 19 and equation (9)
- Confidence rationale: Explicit theorem relating to Kauffman bracket
- Uncertainties: None
- Cross-reference status: Verified
