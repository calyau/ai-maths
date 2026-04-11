---
concept: Third Sylow Theorem
slug: third-sylow-theorem
category: group-theory
subcategory: group-actions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 142
section: "4.5 Sylow's Theorem"
extraction_confidence: high
aliases:
  - "Sylow counting theorem"
  - "Sylow III"
  - "Sylow congruence theorem"
prerequisites:
  - first-sylow-theorem
  - second-sylow-theorem
  - sylow-p-subgroup
  - normalizer
extends:
  - second-sylow-theorem
related:
  - first-sylow-theorem
contrasts_with: []
answers_questions:
  - "How many Sylow p-subgroups can a group have?"
  - "How do I apply the Sylow theorems to analyze group structure?"
---

# Quick Definition
The number of Sylow p-subgroups, n_p, satisfies n_p = 1 (mod p) and n_p divides m, where |G| = p^a * m with gcd(p, m) = 1. Furthermore, n_p = |G : N_G(P)| for any Sylow p-subgroup P.

# Core Definition
Theorem 18(3): The number of Sylow p-subgroups of G is of the form 1 + kp, i.e., n_p is congruent to 1 (mod p). Further, n_p is the index in G of the normalizer N_G(P) for any Sylow p-subgroup P, hence n_p divides m (Dummit & Foote, p. 142). The proof that n_p is congruent to 1 mod p uses P acting on its own conjugacy class by conjugation.

# Prerequisites
- **First Sylow theorem** — Existence is needed first
- **Second Sylow theorem** — Conjugacy implies n_p = |G : N_G(P)|
- **Sylow p-subgroup** — The objects being counted
- **Normalizer** — n_p equals the index of the normalizer

# Key Properties
1. n_p is congruent to 1 mod p
2. n_p divides m (where |G| = p^a * m, gcd(p,m) = 1)
3. n_p = |G : N_G(P)| for any P in Syl_p(G)
4. n_p = 1 iff the Sylow p-subgroup is normal
5. These two divisibility constraints often severely restrict possible values of n_p

# Construction / Recognition
## To Apply the Third Sylow Theorem:
1. Factor |G| = p^a * m
2. List all divisors of m that are congruent to 1 mod p
3. These are the only possible values for n_p
4. If the only possibility is n_p = 1, the Sylow p-subgroup is normal

# Context & Application
The Third Sylow Theorem is the primary tool for proving groups of specific orders are not simple. The congruence constraint is particularly powerful for large primes p dividing |G|, often forcing n_p = 1.

# Examples
**Example 1** (p. 147): For |G| = pq with p < q primes: n_q divides p and n_q is congruent to 1 mod q. Since p < q, n_q = 1, so the Sylow q-subgroup is normal.

**Example 2** (p. 148): For |G| = 30 = 2 * 3 * 5: n_5 is 1 or 6, n_3 is 1 or 10. If both n_5 = 6 and n_3 = 10, element counting gives 24 + 20 = 44 elements of order 5 or 3, which is impossible. So at least one is normal.

**Example 3** (p. 148): For |G| = 12: n_3 divides 4 and n_3 is congruent to 1 mod 3, so n_3 = 1 or 4.

# Relationships
## Builds Upon
- **Second Sylow theorem** — Conjugacy implies n_p = |G : N_G(P)|
## Enables
- **Simplicity analysis** — Used to prove groups are not simple
- **Group classification** — Constrains possible group structures

# Common Errors
- **Error**: Forgetting that n_p must satisfy BOTH conditions (congruence and divisibility)
  **Correction**: n_p must simultaneously be congruent to 1 mod p AND divide m

- **Error**: Concluding n_p = 1 when the only constraint is the congruence condition
  **Correction**: Both constraints must be checked together

# Common Confusions
- **Confusion**: Believing the Sylow congruence completely determines n_p
  **Clarification**: The congruence only constrains n_p; additional arguments (counting elements, permutation representations) may be needed to pin down the exact value

# Source Reference
Chapter 4: Group Actions, Section 4.5, Theorem 18(3), pages 142-146.

# Verification Notes
- Definition source: Direct from Theorem 18(3), p. 142
- Confidence: HIGH — stated and proved
- Uncertainties: None
