---
# === CORE IDENTIFICATION ===
concept: "Sylow's Second Theorem (Conjugacy and Containment)"
slug: sylow-second-theorem

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
pdf_page: 78
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Sylow II
  - conjugacy of Sylow subgroups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - sylow-first-theorem
  - group-action
  - p-group-fixed-point-lemma
  - sylow-normalizer-lemma
extends:
  - sylow-first-theorem
related:
  - number-of-sylow-p-subgroups
  - sylow-third-theorem
  - unique-sylow-subgroup-criterion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are all Sylow p-subgroups related to each other?"
  - "Is every p-subgroup contained in a Sylow p-subgroup?"
  - "How do I compute the number of Sylow p-subgroups?"
---

# Quick Definition

All Sylow p-subgroups of a finite group are conjugate to each other, every p-subgroup is contained in a Sylow p-subgroup, and the number of Sylow p-subgroups satisfies s_p congruent to 1 mod p with s_p dividing m (where |G| = p^r m).

# Core Definition

**Theorem 5.6 (Sylow II).** Let G be a finite group with |G| = p^r m, p not dividing m.

(a) Any two Sylow p-subgroups are conjugate.
(b) The number s_p of Sylow p-subgroups satisfies s_p congruent to 1 mod p, and s_p divides m.
(c) Every p-subgroup of G is contained in a Sylow p-subgroup.

(Milne, Theorem 5.6, p. 78)

# Prerequisites

- **sylow-p-subgroup** -- the objects being compared
- **sylow-first-theorem** -- existence of at least one Sylow p-subgroup
- **group-action** -- proof uses conjugation action on the set of Sylow subgroups
- **p-group-fixed-point-lemma** -- key tool: |X| congruent to |X^P| mod p
- **sylow-normalizer-lemma** -- Lemma 5.7: if a p-subgroup normalizes a Sylow p-subgroup P, it is contained in P

# Key Properties

1. Conjugacy (a): there is essentially one Sylow p-subgroup up to conjugation
2. Counting (b): s_p = (G : N_G(P)) divides (G : 1)/p^r = m, and s_p congruent to 1 mod p
3. Maximality (c): Sylow p-subgroups are the maximal p-subgroups
4. The number s_p equals the index of the normalizer: s_p = (G : N_G(P))

# Construction / Recognition

## Proof Sketch (Conjugacy):
1. Let X be the set of all Sylow p-subgroups; G acts on X by conjugation
2. Fix P in X; let P act on the orbit O of P
3. The only fixed point of P on O is P itself (by Lemma 5.7)
4. So |O| congruent to 1 mod p
5. If P' were outside O, then P acting on O would have no fixed points, giving p | |O|, contradiction
6. Hence O = X: all Sylow p-subgroups are conjugate

## Proof Sketch (Containment):
1. Let H be a p-subgroup; let H act on X by conjugation
2. Since |X| = s_p is not divisible by p, the fixed point lemma gives a fixed point P
3. H normalizes P, so Lemma 5.7 gives H subset of P

# Context & Application

Conjugacy means that any structural property of one Sylow p-subgroup (e.g., being abelian, cyclic) holds for all of them. The counting constraints on s_p are the main tool for classifying groups of small order and for proving non-simplicity results.

# Examples

**Example 1** (p. 81, 5.13): For |G| = 99 = 9 * 11, we get s_11 | 9 and s_11 congruent to 1 mod 11, so s_11 = 1. Similarly s_3 | 11 and s_3 congruent to 1 mod 3, so s_3 = 1.

**Example 2** (p. 80, 5.10): For GL_n(F_p), the Sylow p-subgroups are exactly the groups U(F) for maximal flags F, and conjugacy corresponds to the fact that gU(F)g^{-1} = U(gF).

# Relationships

## Builds Upon
- **sylow-first-theorem** -- existence is needed before discussing conjugacy

## Enables
- **unique-sylow-subgroup-criterion** -- normal iff unique
- **number-of-sylow-p-subgroups** -- the constraints from part (b)
- **direct-product-of-sylow-subgroups** -- when all Sylow subgroups are normal

## Related
- **normalizer-and-sylow** -- s_p = (G : N_G(P))

# Common Errors

- **Error**: Forgetting that s_p must divide m (not |G|)
  **Correction**: s_p divides the p'-part m of |G|, not |G| itself

# Common Confusions

- **Confusion**: Thinking conjugacy implies the Sylow p-subgroups are equal
  **Clarification**: Conjugate means gPg^{-1} = Q for some g; they are equal only when the Sylow subgroup is normal (unique)

# Source Reference

Chapter 5, Theorem 5.6 and Lemma 5.7, pp. 78-79.

# Verification Notes

- Definition source: Direct from Theorem 5.6, p. 78
- Confidence rationale: HIGH -- explicitly stated theorem with full proof
- Uncertainties: None
