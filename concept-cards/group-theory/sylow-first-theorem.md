---
# === CORE IDENTIFICATION ===
concept: "Sylow's First Theorem (Existence)"
slug: sylow-first-theorem

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 77
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Sylow I
  - existence of Sylow subgroups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - group-action
  - p-group
  - sylow-p-subgroup
extends: []
related:
  - sylow-second-theorem
  - sylow-third-theorem
  - cauchys-theorem-from-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find the Sylow p-subgroups of a finite group?"
  - "Do Sylow p-subgroups always exist?"
  - "What must I know before understanding the Sylow theorems?"
---

# Quick Definition

For any finite group G and any prime power p^r dividing |G|, there exists a subgroup of G of order p^r. In particular, Sylow p-subgroups always exist.

# Core Definition

**Theorem 5.2 (Sylow I).** Let G be a finite group, and let p be a prime. If p^r divides (G : 1), then G has a subgroup of order p^r.

(Milne, Theorem 5.2, p. 77)

# Prerequisites

- **group-action** -- the proof uses G acting on the set of p^r-element subsets
- **sylow-p-subgroup** -- the theorem establishes the existence of these subgroups
- **p-group** -- subgroups of prime-power order are p-groups

# Key Properties

1. The theorem guarantees subgroups of *every* prime-power order dividing |G|, not just the maximal one
2. The proof is combinatorial: G acts on the set X of subsets of G with p^r elements
3. The key observation is that the binomial coefficient C(p^r m, p^r) is not divisible by p
4. Thus some orbit has size not divisible by p, and the stabilizer of a set in that orbit has order p^r

# Construction / Recognition

## Proof Strategy (Milne's approach):
1. Write |G| = p^r m with gcd(p, m) = 1
2. Let X = {subsets of G with p^r elements}
3. G acts on X by left multiplication: (g, A) -> gA
4. For A in X, Stab(A) has order at most p^r (since h -> ha_0 is injective for any a_0 in A)
5. Show |X| = C(p^r m, p^r) is not divisible by p
6. Hence some orbit has size not divisible by p, forcing |Stab(A)| = p^r

## Alternative Proof (5.12):
Embed G into GL_n(F_p) via Cayley's theorem, then use that GL_n(F_p) has a known Sylow p-subgroup (the unitriangular matrices).

# Context & Application

This is the foundational existence theorem for Sylow theory. It strengthens Cauchy's theorem (which only gives elements of prime order) to give subgroups of any prime-power order dividing |G|. Combined with Sylow II and III, it provides the main structural tool for analyzing finite groups.

# Examples

**Example 1** (p. 77, 5.3): For GL_n(F_p), the unitriangular matrices form a Sylow p-subgroup of order p^(n(n-1)/2), providing an explicit construction.

**Example 2** (p. 77, Remark 5.4): As a corollary, if p divides |G|, then G contains an element of order p (recovering Cauchy's theorem).

# Relationships

## Builds Upon
- **group-action** -- the proof is an application of group actions on combinatorial sets

## Enables
- **sylow-second-theorem** -- conjugacy and containment depend on existence
- **cauchys-theorem-from-sylow** -- Cauchy's theorem follows as a special case

## Related
- **sylow-third-theorem** -- constrains the number of Sylow subgroups

# Common Errors

- **Error**: Thinking the theorem only guarantees subgroups of order p^r where p^r is the *highest* power of p dividing |G|
  **Correction**: The theorem guarantees subgroups of order p^r for *every* r with p^r | |G|

# Common Confusions

- **Confusion**: Confusing Sylow I with Cauchy's theorem
  **Clarification**: Cauchy gives an element of order p (hence a cyclic subgroup of order p). Sylow I gives subgroups of order p^r for all valid r, but does not specify their structure.

# Source Reference

Chapter 5, Theorem 5.2, p. 77. Alternative proof via double cosets in Theorem 5.12, p. 80.

# Verification Notes

- Definition source: Direct from Theorem 5.2, p. 77
- Confidence rationale: HIGH -- explicitly stated and proved theorem
- Uncertainties: None
