---
concept: Todd-Coxeter Algorithm
slug: todd-coxeter-algorithm
category: group-theory
subcategory: generators-and-relations
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.11 The Todd-Coxeter Algorithm"
extraction_confidence: high
aliases: []
prerequisites:
  - presentation-of-group
  - operation-on-cosets
extends: []
related:
  - word-problem
contrasts_with: []
answers_questions:
  - "How can I determine the coset structure of a finitely presented group?"
---

# Quick Definition

The Todd-Coxeter Algorithm is a method for determining the operation of a finitely presented group G on the cosets of a subgroup H. It constructs a table of coset representatives by systematically applying generators and enforcing relations.

# Core Definition

The Todd-Coxeter Algorithm determines the operation of G = <x_1, ..., x_m | r_1, ..., r_k> on the right cosets of a subgroup H given by generators h_1, ..., h_s (Artin, Section 7.11, p. 228). The algorithm uses four rules: (1) each generator acts as a permutation, (2) relations fix every coset, (3) generators of H fix [H], (4) the action is transitive. It terminates for finite groups and produces the correct permutation representation (Theorem 7.11.10).

# Prerequisites

- **Presentation of a group** — The input is a group presentation
- **Operation on cosets** — The output is the coset action

# Key Properties

1. Terminates when G is finite
2. Produces the correct permutation representation (Theorem 7.11.10)
3. Determines the index [G : H]
4. Can determine |G| when combined with |H|
5. When H = {1}, the cosets correspond to group elements

# Construction / Recognition

## Algorithm Steps:
1. Start with index 1 for coset [H]
2. Apply generators of H to fix index 1 (Rule 3)
3. For undetermined operations, assign new indices (Rule 4)
4. Use relations to deduce or equate indices (Rule 2)
5. Continue until all operations are determined

# Context & Application

The Todd-Coxeter Algorithm is a practical tool for understanding finitely presented groups. It can determine the order of the group, verify that a set of relations is complete, and find the permutation representation on cosets. Artin uses it to verify that the tetrahedral group has order 12 and to show that bad relations can collapse a group.

# Examples

**Example 1** (p. 228): For G = <x, y, z | x^3, y^2, z^2, xyz> and H = <z>, the algorithm gives 3 cosets with x = (123), y = (12), z = (23). So [G:H] = 3, |H| = 2, and |G| = 6 = S_3.

**Example 2** (p. 229): For T = <x, y | x^3, y^3, xyxy> and H = <x>, the algorithm gives 4 cosets with x = (234), y = (123). So [T:H] = 4, |H| = 3, and |T| = 12 = A_4.

**Example 3** (p. 230): For <x, y | x^3, y^3, yxyxy> and H = <y>, the algorithm collapses to 1 coset, so G = H = C_3.

# Relationships

## Builds Upon
- **Presentation of a group** — The input
- **Operation on cosets** — The output

## Related
- **Word problem** — The algorithm implicitly solves special cases

# Common Errors

- **Error**: Making a mistake in the table causes the operation to collapse
  **Correction**: Care is essential; verify each step

# Source Reference

Chapter 7: More Group Theory, Section 7.11, Rules 7.11.3, Theorem 7.11.10, pages 228-233.

# Verification Notes

- Definition source: From Section 7.11 and Rules 7.11.3
- Confidence rationale: Extensively developed with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
