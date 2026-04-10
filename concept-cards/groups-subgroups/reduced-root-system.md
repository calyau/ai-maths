---
concept: Reduced Root System
slug: reduced-root-system
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 297
section: "Root systems and their classification"
extraction_confidence: high
aliases: []
prerequisites:
  - root-system
extends: []
related:
  - indecomposable-root-system
contrasts_with: []
answers_questions:
  - "What is a reduced root system?"
---

# Quick Definition

A root system is reduced if, for each root α, the only roots that are scalar multiples of α are ±α. Milne's convention is that "root system" means "reduced root system."

# Core Definition

For each root α in a root system R, the set of roots that are multiples of α is either {−α, α} or {−α, −α/2, α/2, α}. When only the first case occurs, the root system is **reduced** (Milne, p. 297).

From this point on in Milne's text, "root system" means "reduced root system."

# Prerequisites

- **Root system** — Reducedness is a property of root systems

# Key Properties

1. All root systems arising from semisimple Lie algebras are reduced (Theorem 2.23)
2. All root systems arising from split reductive groups are reduced
3. The non-reduced case (type BC_n) can arise in other contexts

# Source Reference

Chapter III, Section 1b, page 297.

# Verification Notes

- Definition source: Direct from p. 297
- Confidence: HIGH
- Uncertainties: None
