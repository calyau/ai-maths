---
concept: Regular Representation
slug: regular-representation
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.6 The Regular Representation"
extraction_confidence: high
aliases: []
prerequisites: [group-representation, permutation-representation-ch10]
extends: [group-representation]
related: [main-theorem-on-characters]
contrasts_with: []
answers_questions: ["What is the regular representation?"]
---
# Quick Definition
The regular representation of G is the permutation representation associated to the operation of G on itself by left multiplication. Its character satisfies chi^reg(1) = |G| and chi^reg(g) = 0 for g != 1. It contains every irreducible representation with multiplicity equal to its dimension.
# Core Definition
The regular representation rho^reg of G is the representation on the vector space V_G with basis {e_g} indexed by group elements, where rho_g(e_h) = e_{gh} (Artin, (10.6.8), p. 317). Its character is chi^reg(1) = |G| and chi^reg(g) = 0 for g != 1 (10.6.9). Corollary 10.6.11: chi^reg = d_1 chi_1 + ... + d_r chi_r, where d_i = dim chi_i. Counting dimensions gives |G| = d_1^2 + ... + d_r^2 (10.6.12).
# Prerequisites
- **Group representation** — The regular representation is a specific representation
# Key Properties
1. Dimension = |G|
2. chi^reg(1) = |G|, chi^reg(g) = 0 for g != 1
3. Each irreducible appears with multiplicity equal to its dimension: rho^reg = d_1 rho_1 + ... + d_r rho_r
4. (chi^reg, chi) = chi(1) = dim chi for any character chi (10.6.10)
5. Proves |G| = d_1^2 + ... + d_r^2 (part (c) of Main Theorem)
# Context & Application
The regular representation is a universal representation containing all irreducibles. It provides a simple proof of the dimension formula in the Main Theorem, and it is a key tool for constructing character tables.
# Examples
**Example 1** (p. 319): For S_3: chi^reg = (6, 0, 0, 0, 0, 0). Decomposition: chi^reg = chi_1 + chi_2 + 2 chi_3.
# Relationships
## Builds Upon
- **Group representation** — A specific representation
## Enables
- **Main theorem on characters** — The dimension formula follows from the regular representation
# Source Reference
Chapter 10: Group Representations, Section 10.6, pages 317-319.
# Verification Notes
- Definition source: Direct from (10.6.8) and (10.6.9)
- Confidence rationale: Explicitly defined with key decomposition formula
- Uncertainties: None
- Cross-reference status: Verified
