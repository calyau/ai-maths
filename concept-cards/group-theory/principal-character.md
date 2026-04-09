---
# === CORE IDENTIFICATION ===
concept: Principal Character
slug: principal-character

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
pdf_page: 114
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "trivial character"
  - "chi_1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-a-representation
extends:
  - irreducible-character
related:
  - one-dimensional-representation
contrasts_with:
  - regular-character

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the principal character?"
  - "What is the trivial character?"
---

# Quick Definition

The principal character chi_1 is the character of the trivial representation: chi_1(g) = 1 for all g in G.

# Core Definition

The **principal character** chi_1 is the character defined by the trivial representation of G (where every g acts as the identity on a 1-dimensional space). So chi_1(g) = 1 for all g in G. (Milne, Chapter 7, p. 114)

# Prerequisites

- **Character of a representation** — the principal character is a specific character

# Key Properties

1. chi_1(g) = 1 for all g in G
2. It is irreducible (the trivial representation is 1-dimensional, hence simple)
3. It is a linear character (degree 1)

# Construction / Recognition

1. The trivial representation: rho(g) = 1 for all g
2. Its character: chi_1(g) = Tr(1) = 1

# Context & Application

The principal character is always one of the irreducible characters. It corresponds to the factor M_1(F) = F in the decomposition F[G] = M_{f_1}(F) x ... x M_{f_t}(F) (by convention, S_1 is chosen to be the trivial representation).

# Examples

**Example 1** (p. 117, 7.54): In the character table of S_3, the first row chi_0 is the trivial character: all entries are 1.

# Relationships

## Builds Upon
- **character-of-a-representation** — specific character
- **irreducible-character** — it is irreducible

## Enables
- A reference point in the character table (always row 1)

## Related
- **one-dimensional-representation** — the trivial representation is 1-dimensional

## Contrasts With
- **regular-character** — chi_reg(g) = 0 for g != e, while chi_1(g) = 1 always

# Source Reference

Chapter 7: Representations of Finite Groups, p. 114.

# Verification Notes

- Definition source: Direct from p. 114
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
