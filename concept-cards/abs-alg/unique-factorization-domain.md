---
concept: Unique Factorization Domain
slug: unique-factorization-domain
category: ring-theory
subcategory: special-domains
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 283
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases:
  - "UFD"
  - "U.F.D."
  - "factorial ring"
prerequisites:
  - integral-domain
  - irreducible-element
extends:
  - integral-domain
related:
  - principal-ideal-domain
  - euclidean-domain
  - irreducible-element
  - prime-element
  - associates
contrasts_with:
  - principal-ideal-domain
answers_questions:
  - "What is a UFD?"
  - "How do Euclidean domains, PIDs, and UFDs relate to each other?"
---

# Quick Definition
A Unique Factorization Domain (UFD) is an integral domain where every nonzero non-unit can be written as a finite product of irreducibles, and this factorization is unique up to order and associates.

# Core Definition
A *Unique Factorization Domain* (U.F.D.) is an integral domain R in which every nonzero element $r$ that is not a unit has the following properties: (i) r can be written as a finite product of irreducibles: $r = p_1 p_2 \cdots p_n$, and (ii) this decomposition is unique up to associates: if $r = q_1 q_2 \cdots q_m$ is another factorization into irreducibles, then $m = n$ and after renumbering, $p_i$ is associate to $q_i$ (Dummit & Foote, pp. 285-286).

# Prerequisites
- **Integral domain** — A UFD is a special integral domain
- **Irreducible element** — Factorization is into irreducibles

# Key Properties
1. Every PID is a UFD (Theorem 14, p. 286)
2. In a UFD, irreducible iff prime (Proposition 12, p. 286)
3. Any two nonzero elements have a GCD (Proposition 13, p. 287)
4. $R[x]$ is a UFD whenever R is a UFD (Theorem 7, Ch. 9)
5. Fields $\subset$ Euclidean Domains $\subset$ PIDs $\subset$ UFDs $\subset$ integral domains (p. 290)
6. The Fundamental Theorem of Arithmetic: $\mathbb{Z}$ is a UFD (Corollary 15, p. 289)

# Construction / Recognition
## To Verify:
1. Confirm R is an integral domain
2. Show every nonzero non-unit factors into irreducibles (existence)
3. Show the factorization is unique up to associates (uniqueness)

## To Show R is NOT a UFD:
1. Find two distinct factorizations of the same element into irreducibles
2. Find an irreducible element that is not prime

# Context & Application
UFDs generalize the Fundamental Theorem of Arithmetic to abstract rings. The UFD property is preserved under polynomial ring extension ($R$ UFD $\Rightarrow$ $R[x]$ UFD), unlike the PID or Euclidean properties.

# Examples
**Example 1** (p. 289): $\mathbb{Z}$ is a UFD (Fundamental Theorem of Arithmetic).

**Example 2** (p. 286): $F[x]$ for a field F is a UFD.

**Example 3** (p. 286): $\mathbb{Z}[x]$ is a UFD but not a PID.

**Example 4** (p. 287): $\mathbb{Z}[\sqrt{-5}]$ is NOT a UFD: $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$.

**Example 5** (p. 286): $\mathbb{Z}[2i]$ is NOT a UFD: $4 = 2 \cdot 2 = (-2i)(2i)$.

# Relationships

## Builds Upon
- **integral-domain** — With unique factorization property

## Related
- **irreducible-element** — Factorizations are into irreducibles
- **prime-element** — In a UFD, irreducible = prime
- **associates** — Uniqueness is up to associates

## Contrasts With
- **principal-ideal-domain** — Every PID is a UFD, but $\mathbb{Z}[x]$ is a UFD that is not a PID

# Common Errors
- **Error**: Assuming every UFD is a PID
  **Correction**: $\mathbb{Z}[x]$ is a UFD but not a PID

# Common Confusions
- **Confusion**: Thinking unique factorization means literally unique
  **Clarification**: Factorizations are unique only *up to order and associates*; e.g., $6 = 2 \cdot 3 = 3 \cdot 2 = (-2)(-3)$ in $\mathbb{Z}$

# Source Reference
Chapter 8, Section 8.3, Definition on pages 285-286. See Theorem 14 on page 286 and Proposition 12 on page 286.

# Verification Notes
- Definition: Direct from pp. 285-286
- Key results: Theorem 14, Propositions 12-13
- Confidence: HIGH — explicit definition with rich examples
