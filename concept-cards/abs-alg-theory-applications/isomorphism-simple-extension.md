---
concept: Isomorphism of Simple Extensions
slug: isomorphism-simple-extension
category: field-theory
subcategory: field-extensions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"
extraction_confidence: high
aliases: []
prerequisites:
  - simple-extension
  - minimal-polynomial
  - factor-ring
extends: []
related:
  - kronecker-theorem
contrasts_with: []
answers_questions:
  - "How is F(alpha) related to F[x]/<p(x)>?"
---

# Quick Definition

If $\alpha$ is algebraic over $F$ with minimal polynomial $p(x)$, then $F(\alpha) \cong F[x]/\langle p(x) \rangle$. This isomorphism is the fundamental structural result for simple algebraic extensions.

# Core Definition

**Proposition 21.12.** Let $E$ be a field extension of $F$ and $\alpha \in E$ be algebraic over $F$. Then $F(\alpha) \cong F[x]/\langle p(x) \rangle$, where $p(x)$ is the minimal polynomial of $\alpha$ over $F$ (Judson, p. 277).

# Prerequisites

- **Simple extension** — $F(\alpha)$ is a simple extension
- **Minimal polynomial** — Determines the quotient structure
- **Factor ring** — The quotient $F[x]/\langle p(x) \rangle$ is a factor ring

# Key Properties

1. The isomorphism sends $\alpha$ to $x + \langle p(x) \rangle$
2. This makes $F(\alpha)$ a field with $[F(\alpha):F] = \deg p(x)$
3. Arithmetic in $F(\alpha)$ reduces to polynomial arithmetic modulo $p(x)$
4. This is the theoretical basis for Kronecker's construction (Theorem 21.5)

# Examples

**Example 1** (p. 278): $\mathbb{R}[x]/\langle x^2 + 1 \rangle \cong \mathbb{C}$ via $\alpha = x + \langle x^2 + 1 \rangle \mapsto i$.

**Example 2** (p. 275): $\mathbb{Z}_2[x]/\langle x^2 + x + 1 \rangle \cong \mathbb{Z}_2(\alpha)$ where $\alpha^2 + \alpha + 1 = 0$.

# Relationships

## Builds Upon
- **Simple extension** — The extension $F(\alpha)$
- **Minimal polynomial** — The modulus $p(x)$

## Related
- **Kronecker's Theorem** — Uses this construction

# Source Reference

Chapter 21: Fields, Section 21.1, page 277. Proposition 21.12.

# Verification Notes

- Definition source: Direct from Proposition 21.12, p. 277
- Confidence: HIGH — explicit proposition
- Cross-reference status: Verified
- Uncertainties: None
