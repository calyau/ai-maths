---
# === CORE IDENTIFICATION ===
concept: Semigroup
slug: semigroup

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 10
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - magma
extends:
  - magma
related:
  - monoid
  - group
contrasts_with:
  - group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a semigroup?"
  - "What is the difference between a semigroup and a group?"
---

# Quick Definition

A semigroup is a set with an associative binary operation. Unlike a group, it need not have a neutral element or inverses.

# Core Definition

When the binary operation on a magma (S, .) is associative, (S, .) is called a **semigroup** (Remark 1.9, p. 10). The product of any finite sequence of elements in a semigroup is well-defined.

# Prerequisites

- **Magma** — a semigroup is an associative magma

# Key Properties

1. Has a closed binary operation (from magma)
2. The operation is associative
3. Products of any finite nonempty sequence are well-defined (Equation 8, p. 10)
4. No neutral element or inverses required

# Construction / Recognition

## To Recognize:
1. Check that the binary operation is closed
2. Check associativity: (a . b) . c = a . (b . c) for all a, b, c

# Context & Application

Semigroups sit between magmas and monoids in the algebraic hierarchy. Milne introduces them to motivate the group axioms: the question "what should the empty product be?" leads naturally to requiring a neutral element (monoid), and then inverses complete the passage to a group.

# Examples

**Example 1** (p. 11, Aside 1.10b): (N, +) is a semigroup satisfying associativity and nonemptiness but not the inverse axiom, showing it is a semigroup but not a group.

# Relationships

## Builds Upon
- **magma** — a semigroup is a magma with associativity

## Enables
- **monoid** — a semigroup with a neutral element

## Contrasts With
- **group** — a group has a neutral element and inverses; a semigroup may lack both

# Common Confusions

- **Confusion**: Thinking every semigroup has an identity element
  **Clarification**: A semigroup with an identity is called a monoid; not all semigroups are monoids

# Source Reference

Chapter 1: Basic Definitions and Results, Remark 1.9, page 10.

# Verification Notes

- Definition source: Direct from Remark 1.9, p. 10
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
