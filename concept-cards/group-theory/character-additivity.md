---
# === CORE IDENTIFICATION ===
concept: Character Additivity
slug: character-additivity

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
extends: []
related:
  - completely-reducible-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the character behave under direct sums?"
---

# Quick Definition

For F[G]-modules V and V', chi_{V+V'} = chi_V + chi_{V'}. Characters are additive under direct sums.

# Core Definition

**Lemma 7.42.** For all F[G]-modules V and V', chi_{V + V'} = chi_V + chi_{V'}. The proof computes the trace with respect to a basis that is the union of bases for V and V'. (Milne, Lemma 7.42, p. 115)

# Prerequisites

- **Character of a representation** — additivity is a property of characters

# Key Properties

1. chi_{V+W} = chi_V + chi_W
2. chi_{mV} = m chi_V
3. Any character is a non-negative integer combination of irreducible characters
4. This is why characters of completely reducible representations determine the multiplicities

# Examples

**Example 1** (p. 115): If V = S_1 + S_1 + S_2, then chi_V = 2 chi_1 + chi_2.

# Relationships

## Builds Upon
- **character-of-a-representation** — additivity is a fundamental property

## Enables
- Decomposition of characters into irreducible characters
- **characters-determine-representations** — via the multiplicity formula

# Source Reference

Chapter 7: Representations of Finite Groups, Lemma 7.42, p. 115.

# Verification Notes

- Definition source: Direct from Lemma 7.42
- Confidence rationale: HIGH — explicit lemma
- Uncertainties: None
