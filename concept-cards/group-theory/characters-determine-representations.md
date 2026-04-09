---
# === CORE IDENTIFICATION ===
concept: Characters Determine Representations
slug: characters-determine-representations

# === CLASSIFICATION ===
category: character-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 115
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-a-representation
  - irreducible-character
extends: []
related:
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Do characters determine representations up to isomorphism?"
  - "When do two representations with the same character have to be isomorphic?"
---

# Quick Definition

Over an algebraically closed field of characteristic zero, two F[G]-modules are isomorphic if and only if they have the same character.

# Core Definition

**Proposition 7.44.** Two F[G]-modules are isomorphic if and only if their characters are equal. (Milne, Proposition 7.44, p. 115)

The proof uses the central idempotents e_j: if V = direct sum c_i S_i, then chi_V = sum c_i chi_i, and c_i = chi_V(e_i)/f_i, so the character determines the multiplicities.

# Prerequisites

- **Character of a representation** — the function being compared
- **Irreducible character** — characters decompose into irreducible characters

# Key Properties

1. Over algebraically closed fields of characteristic zero, character = isomorphism class
2. This fails in characteristic p != 0 (Aside 7.45): the matrix (1, i; 0, 1) representation of C_p has the same character as the trivial rep but is not isomorphic
3. The multiplicities c_i are recovered from the character via central idempotents
4. This is the fundamental reason character theory works

# Construction / Recognition

To check if two modules are isomorphic:
1. Compute their characters
2. If chi_V = chi_W, then V is isomorphic to W
3. Alternatively, compare the inner products (chi_V | chi_i) for each irreducible chi_i

# Context & Application

This proposition is the cornerstone of character theory: it reduces the classification of representations to the study of class functions. Without this, character theory would be merely a partial invariant rather than a complete one.

# Examples

**Example 1** (p. 115, Aside 7.45): Over a field of characteristic p, the 2-dimensional representation of C_p via (1, i; 0, 1) has the same character as the trivial 2-dimensional representation, but they are not isomorphic. So the result requires characteristic zero.

# Relationships

## Builds Upon
- **character-of-a-representation** — the invariant
- **irreducible-character** — decomposition into irreducibles

## Enables
- Character theory as a complete invariant for representations
- **character-table** — a complete description of representation theory

## Related
- **decomposition-of-f-g** — provides the structure making this work

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.44 and Aside 7.45, p. 115.

# Verification Notes

- Definition source: Direct from Proposition 7.44
- Confidence rationale: HIGH — explicit proposition
- Uncertainties: None
