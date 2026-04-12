---
# === CORE IDENTIFICATION ===
concept: Groups of Order pq
slug: groups-of-order-pq

# === CLASSIFICATION ===
category: automorphisms
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Automorphisms"
chapter_number: 23
pdf_page: 138
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 23.2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism-group
  - normal-subgroup
  - lagrange-theorem
extends: []
related:
  - semidirect-product
  - direct-product
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a group of order pq cyclic?"
  - "What distinguishes a direct product from a semidirect product?"
---

# Quick Definition

If p, q are primes with p > q and q does not divide (p - 1), then every group of order pq is cyclic. This is proved using automorphism theory: the conjugation action of an element of order q on the Sylow p-subgroup must be trivial.

# Core Definition

"(23.2) Theorem. If p, q are primes which satisfy p > q and q does not divide (p - 1), then every group of order pq is cyclic" (Armstrong, Ch. 23, p. 138). The proof shows the Sylow p-subgroup H is normal, then uses the fact that the conjugation automorphism of H induced by an element of order q has order dividing both q and |Aut(H)| = p - 1. Since q does not divide p - 1, this automorphism is trivial, so the elements commute and G is the direct product Z_p x Z_q, which is cyclic.

# Prerequisites

- **Automorphism group** -- |Aut(Z_p)| = p - 1 constrains the conjugation action
- **Normal subgroup** -- The Sylow p-subgroup is shown to be normal
- **Lagrange's theorem** -- Used to constrain the order of the conjugation automorphism

# Key Properties

1. p > q are primes with q not dividing (p - 1)
2. The Sylow p-subgroup H = <x> is normal in G
3. Conjugation by y (of order q) gives an automorphism of H of order dividing both q and p - 1
4. Since q does not divide p - 1, this order is 1 (trivial automorphism)
5. Therefore yh = hy for all h in H, giving G = H x K = Z_p x Z_q = Z_{pq}

# Construction / Recognition

## Proof Strategy (Armstrong, p. 138)
1. Choose x of order p, y of order q; set H = <x>
2. Show H is normal using a coset-counting argument
3. The conjugation map h -> yhy^{-1} is an automorphism of H
4. Its order divides q (since y^q = e) and divides p - 1 (since |Aut(Z_p)| = p - 1)
5. Since q does not divide p - 1, the order is 1
6. Elements of H and K = <y> commute; HK = G, H intersect K = {e}
7. Therefore G = Z_p x Z_q = Z_{pq}

# Context & Application

This theorem demonstrates the power of automorphism theory in classifying groups. It shows that for certain orders pq, the only group structure is the direct product (no non-trivial semidirect products exist). When q does divide p - 1, non-cyclic groups of order pq can exist as semidirect products.

# Examples

**Example 1**: Every group of order 15 (= 5 x 3) is cyclic, since 3 does not divide 4 = 5 - 1.

**Example 2**: Every group of order 35 (= 7 x 5) is cyclic, since 5 does not divide 6 = 7 - 1.

**Counterexample**: Groups of order 6 (= 3 x 2) need not be cyclic: 2 divides 2 = 3 - 1, and S_3 is a non-cyclic group of order 6 (a semidirect product Z_3 x_phi Z_2).

# Relationships

## Builds Upon
- **Automorphism group** -- The constraint |Aut(Z_p)| = p - 1 drives the proof

## Related
- **Semidirect product** -- When q | (p-1), non-cyclic semidirect products can exist
- **Direct product** -- The theorem shows G must be a direct product

# Common Errors

- **Error**: Applying the theorem when q divides p - 1
  **Correction**: The theorem requires q does NOT divide p - 1; when it does, non-cyclic groups may exist

# Common Confusions

- **Confusion**: Thinking all groups of prime-times-prime order are cyclic
  **Clarification**: Only when the smaller prime does not divide one less than the larger prime; S_3 (order 6) is a counterexample

# Source Reference

Chapter 23: Automorphisms, Theorem 23.2 and proof, pages 131-132 (pdf pp. 138-139).

# Verification Notes

- Theorem: Directly quoted from Armstrong p. 138
- Proof: Complete in source
- Confidence: HIGH -- named theorem with complete proof
- Cross-references: Verified against planned extractions
- Uncertainties: None
