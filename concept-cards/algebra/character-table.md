---
concept: Character Table
slug: character-table
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
prerequisites: [character-of-a-representation, irreducible-representation, orthogonality-of-characters]
extends: []
related: [class-function]
contrasts_with: []
answers_questions: ["How do I compute a character table?", "What is a character table?"]
---
# Quick Definition
The character table of a finite group G is a square matrix whose rows are the irreducible characters and whose columns correspond to conjugacy classes. The rows are orthonormal, and the table completely determines the representation theory of G.
# Core Definition
The irreducible characters of a group are assembled into the character table: rows are irreducible characters chi_1, ..., chi_r and columns are conjugacy classes C_1, ..., C_r (Artin, p. 312). By convention, the trivial character is the top row (all 1's) and the first column lists the dimensions (chi(1)). The Main Theorem 10.4.6 guarantees: (a) rows are orthonormal with respect to (chi, chi') = (1/|G|) sum_g chi(g)-bar chi'(g), (b) the number of rows equals the number of columns (conjugacy classes), (c) d_1^2 + ... + d_r^2 = |G|.
# Prerequisites
- **Character of a representation** — The entries of the table
- **Irreducible representation** — Rows correspond to irreducible representations
- **Orthogonality of characters** — Used to compute and verify the table
# Key Properties
1. Square matrix (r x r where r = number of conjugacy classes)
2. Rows are orthonormal with the Hermitian product (10.4.3)
3. Columns are also orthogonal (Exercise 4.6)
4. First column gives dimensions d_i; d_1^2 + ... + d_r^2 = |G|
5. First row is all 1's (trivial character)
6. Any representation can be decomposed using the character table via n_i = (chi, chi_i)
# Construction / Recognition
## To Compute:
1. Determine conjugacy classes and their sizes
2. Determine the number of irreducible representations (= number of classes)
3. Solve |G| = d_1^2 + ... + d_r^2 for dimensions
4. Find one-dimensional characters (from abelianization)
5. Use orthogonality and known representations to fill remaining entries
# Context & Application
The character table is the central computational tool of finite group representation theory. It determines all representations up to isomorphism, reveals normal subgroups (as intersections of kernels of characters), and encodes deep structural information about the group.
# Examples
**Example 1** (p. 312): Character table of S_3: 3 classes, 3 irreducible characters of dimensions 1, 1, 2; chi_1 = (1,1,1), chi_2 = (1,1,-1), chi_3 = (2,-1,0).
**Example 2** (p. 313): Character table of the tetrahedral group T: 4 classes, dimensions 1,1,1,3, with entries involving omega = e^{2pi i/3}.
# Relationships
## Builds Upon
- **Irreducible representation** — Rows of the table
- **Character of a representation** — Entries of the table
- **Orthogonality of characters** — Verification and computation tool
## Enables
- Decomposition of any representation into irreducibles
- Identification of normal subgroups
# Common Errors
- **Error**: Thinking the character table depends on the choice of representative elements
  **Correction**: Characters are constant on conjugacy classes, so any representative works
# Common Confusions
- **Confusion**: Thinking the character table determines the group up to isomorphism
  **Clarification**: Non-isomorphic groups can have the same character table (though this is rare)
# Source Reference
Chapter 10: Group Representations, Section 10.4, pages 312-315. Tables (10.4.12), (10.4.14).
# Verification Notes
- Definition source: Synthesized from Sections 10.1 and 10.4
- Confidence rationale: Extensively developed with examples
- Uncertainties: None
- Cross-reference status: Verified
