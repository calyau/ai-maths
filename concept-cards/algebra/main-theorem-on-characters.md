---
concept: Main Theorem on Characters
slug: main-theorem-on-characters
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.4 Characters"
extraction_confidence: high
aliases: []
prerequisites: [orthogonality-of-characters, irreducible-representation]
extends: []
related: [character-table, regular-representation]
contrasts_with: []
answers_questions: ["What is the main theorem on characters?"]
---
# Quick Definition
The Main Theorem on characters states: (a) irreducible characters are orthonormal, (b) the number of irreducible representations equals the number of conjugacy classes, and (c) the sum of squares of dimensions equals the group order.
# Core Definition
Theorem 10.4.6 (Main Theorem): Let G be a finite group. (a) The irreducible characters are orthonormal. (b) There are finitely many isomorphism classes of irreducible representations, the same number as conjugacy classes. (c) If d_1, ..., d_r are the dimensions, then d_i divides |G| and |G| = d_1^2 + ... + d_r^2 (Artin, p. 311).
# Prerequisites
- **Orthogonality of characters** — Part (a) of the theorem
- **Irreducible representation** — The objects being counted
# Key Properties
1. Orthonormality of irreducible characters (part a)
2. Number of irreducibles = number of conjugacy classes (part b)
3. |G| = d_1^2 + ... + d_r^2 (part c)
4. d_i divides |G| (stated but not proved in Artin)
5. Part (c) follows from parts (a) and the regular representation (10.6.12)
6. Part (b) proved via class functions forming a Hermitian space (Lemma 10.8.5)
# Context & Application
This theorem is the culmination of Chapter 10. It reduces the classification of representations to a finite combinatorial problem (finding character tables). The dimension formula |G| = sum d_i^2 is a powerful constraint.
# Examples
**Example 1** (p. 311): For S_3: 3 conjugacy classes, 3 irreducible representations of dimensions 1, 1, 2. Check: 6 = 1^2 + 1^2 + 2^2.
**Example 2** (p. 313): For the tetrahedral group T: 4 conjugacy classes, dimensions 1, 1, 1, 3. Check: 12 = 1 + 1 + 1 + 9.
# Relationships
## Builds Upon
- **Orthogonality of characters** — Part (a) of the theorem
## Enables
- **Character table** — The theorem guarantees the table is square and provides constraints
# Source Reference
Chapter 10: Group Representations, Section 10.4, Theorem 10.4.6, pages 311-312.
# Verification Notes
- Definition source: Direct from Theorem 10.4.6
- Confidence rationale: Central theorem; parts (a) and (b) proved in Sections 10.8, (c) via regular representation
- Uncertainties: Divisibility of d_i by |G| is stated without proof
- Cross-reference status: Verified
