---
concept: Kauffman Bracket
slug: kauffman-bracket
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 368
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "Kauffman angle bracket"
  - "(L)(A)"
prerequisites:
  - link-diagram
  - reidemeister-moves
  - state-of-link-diagram
extends: []
related:
  - kauffman-square-bracket
  - jones-polynomial
  - one-variable-kauffman-polynomial
contrasts_with:
  - kauffman-square-bracket
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The Kauffman bracket $\langle L \rangle \in \mathbb{Z}[A, A^{-1}]$ is a Laurent polynomial in $A$ defined by evaluating the Kauffman square bracket at $B = A^{-1}$ and $d = -A^2 - A^{-2}$. It is invariant under regular isotopy (Types II and III Reidemeister moves).

# Core Definition
The Kauffman angle bracket (or simply Kauffman bracket) is $(L)(A) = [L](A, A^{-1}, -A^2 - A^{-2})$ (Bollobás, p. 369), where $[L]$ is the Kauffman square bracket. Lemma 17 proves it is invariant under regular isotopy. It satisfies: $\langle L \rangle = A \langle L_v^A \rangle + A^{-1} \langle L_v^B \rangle$ for any crossing $v$.

# Prerequisites
- **Link diagram** — The bracket is defined on link diagrams
- **Reidemeister moves** — Invariance under Types II and III
- **State of a link diagram** — Used in the explicit formula

# Key Properties
1. $\langle L \rangle \in \mathbb{Z}[A, A^{-1}]$ (Laurent polynomial)
2. $\langle \bigcirc \rangle = 1$
3. $\langle L \cup \bigcirc \rangle = (-A^2 - A^{-2}) \langle L \rangle$
4. Recursion: $\langle L \rangle = A \langle L_v^A \rangle + A^{-1} \langle L_v^B \rangle$
5. Invariant under regular isotopy (Types II and III)
6. Under Type I: $\langle \text{curl} \rangle = (-A^3) \langle \text{no curl} \rangle$

# Context & Application
The Kauffman bracket is "perhaps the nicest" of the related link polynomials. It is not quite an ambient isotopy invariant (fails Type I), but multiplying by $(-A)^{-3s(L)}$ (where $s(L)$ is the self-writhe) yields the one-variable Kauffman polynomial, which is an ambient isotopy invariant.

# Examples
**Example** (p. 371): The bracket of the right-handed trefoil knot is $A^{-7} - A^{-3} - A^5$.

# Relationships
## Builds Upon
- **link-diagram**, **reidemeister-moves**, **state-of-link-diagram**

## Enables
- **one-variable-kauffman-polynomial** — $f[L] = (-A)^{-3s(L)} \langle L \rangle$
- **jones-polynomial** — $V_L(t) = f[L](t^{-1/4})$

## Contrasts With
- **kauffman-square-bracket** — More general 3-variable version

# Common Confusions
- **Confusion**: Thinking the Kauffman bracket is an ambient isotopy invariant.
  **Clarification**: It is only a regular isotopy invariant. To get ambient isotopy invariance, multiply by $(-A)^{-3s(L)}$.

# Source Reference
Chapter X, Section X.6, Lemma 17, pages 369-370.

# Verification Notes
- Definition source: Direct from p. 369
- Confidence rationale: Explicit definition with invariance proof
- Uncertainties: None
- Cross-reference status: Verified
