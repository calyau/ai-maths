---
# === CORE IDENTIFICATION ===
concept: Sylow p-Subgroup
slug: sylow-p-subgroup

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
pdf_page: 76
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Sylow subgroup
  - p-Sylow subgroup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - p-group
  - subgroup
  - order-of-a-group
extends:
  - p-group
related:
  - sylow-first-theorem
  - sylow-second-theorem
  - sylow-third-theorem
  - normalizer-and-sylow
contrasts_with:
  - p-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Sylow p-subgroup?"
  - "How do Sylow subgroups relate to the structure of finite groups?"
  - "What must I know before understanding the Sylow theorems?"
---

# Quick Definition

A Sylow p-subgroup of a finite group G is a subgroup whose order is the highest power of p dividing |G|. Equivalently, it is a p-subgroup whose index in G is prime to p.

# Core Definition

Let G be a finite group and let p be a prime dividing (G : 1). Write |G| = p^r m with gcd(p, m) = 1. A subgroup P of G is called a *Sylow p-subgroup* of G if |P| = p^r, that is, if P is a p-group and its index (G : P) = m is prime to p.

(Milne, p. 76)

# Prerequisites

- **group** -- the ambient structure
- **p-group** -- a group whose order is a power of p; Sylow p-subgroups are maximal p-subgroups
- **subgroup** -- Sylow p-subgroups are subgroups with a specific order constraint
- **order-of-a-group** -- the definition depends on the prime factorization of |G|

# Key Properties

1. A Sylow p-subgroup P of G has order p^r where p^r is the largest power of p dividing |G|
2. The index (G : P) is not divisible by p
3. Every p-subgroup of G is contained in some Sylow p-subgroup (Sylow II(c))
4. All Sylow p-subgroups are conjugate in G (Sylow II(a))
5. A Sylow p-subgroup is normal if and only if it is the unique Sylow p-subgroup (Corollary 5.8)

# Construction / Recognition

## To Identify:
1. Compute |G| and factor as p^r m with gcd(p, m) = 1
2. A subgroup P is a Sylow p-subgroup if |P| = p^r
3. Alternatively, check that P is a p-group and (G : P) is coprime to p

## Concrete Construction:
For GL_n(F_p), the upper triangular matrices with 1s on the diagonal form a Sylow p-subgroup of order p^(1+2+...+(n-1)) (Example 5.3).

# Context & Application

Sylow p-subgroups are the fundamental tool for analyzing the structure of finite groups. The Sylow theorems guarantee their existence, describe how they sit inside G (all conjugate), and constrain how many there can be. Applications include classifying groups of small order and proving non-simplicity results.

# Examples

**Example 1** (p. 77, 5.3): In GL_n(F_p), the group of upper unitriangular matrices (upper triangular with 1s on the diagonal) is a Sylow p-subgroup. Its order is p^(1+2+...+(n-1)).

**Example 2** (p. 80, 5.11): In S_4 (order 24 = 2^3 * 3), the Sylow 3-subgroups are the stabilizers of faces of a tetrahedron, and the Sylow 2-subgroups are stabilizers of pairs of opposite edges.

# Relationships

## Builds Upon
- **p-group** -- a Sylow p-subgroup is a maximal p-subgroup

## Enables
- **sylow-first-theorem** -- proves existence of Sylow p-subgroups
- **sylow-second-theorem** -- conjugacy and containment properties
- **sylow-third-theorem** -- counting constraints
- **direct-product-of-sylow-subgroups** -- when all Sylow subgroups are normal

## Related
- **normalizer-and-sylow** -- the normalizer controls conjugacy counting

## Contrasts With
- **p-group** -- a p-group need not be a Sylow p-subgroup; it is only Sylow if it is maximal

# Common Errors

- **Error**: Confusing "p-subgroup" with "Sylow p-subgroup"
  **Correction**: A p-subgroup is any subgroup whose order is a power of p; a Sylow p-subgroup specifically has the *largest* possible order p^r

- **Error**: Assuming there is always a unique Sylow p-subgroup
  **Correction**: There may be multiple Sylow p-subgroups; uniqueness holds exactly when the Sylow p-subgroup is normal (5.8)

# Common Confusions

- **Confusion**: Thinking Sylow p-subgroups for different primes might overlap nontrivially
  **Clarification**: If P is a Sylow p-subgroup and Q is a Sylow q-subgroup with p != q, then P intersect Q = {1}, since any element in the intersection would have order dividing both a power of p and a power of q

# Source Reference

Chapter 5: The Sylow Theorems; Applications, p. 76. Definition at the start of the chapter.

# Verification Notes

- Definition source: Direct from opening paragraph of Chapter 5, p. 76
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
