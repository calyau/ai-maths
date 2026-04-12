---
# === CORE IDENTIFICATION ===
concept: Finitely Presented Group
slug: finitely-presented-group

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Free Groups and Presentations"
chapter_number: 27
pdf_page: 173
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - presentation-of-a-group
  - free-group
extends:
  - presentation-of-a-group
related:
  - defining-relations
contrasts_with:
  - free-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a finitely presented group?"
  - "What distinguishes a free group from a finitely presented group?"
---

# Quick Definition

A finitely presented group is a group that can be described by a finite set of generators and a finite set of defining relations. It has the form {x_1, ..., x_s | w_1, ..., w_t} where the x_i are generators and the w_j are relator words.

# Core Definition

"If X is a finite set with elements x_1, ..., x_s and if R is a finite collection of words w_1, ..., w_t we say that G is finitely presented" (Armstrong, Ch. 27, p. 176). A finitely presented group is the quotient F(x_1,...,x_s)/N where N is the normal closure of {w_1,...,w_t} in the free group.

# Prerequisites

- **Presentation of a group** -- A finitely presented group is one with a finite presentation
- **Free group** -- The presentation is a quotient of a finitely generated free group

# Key Properties

1. Both the generator set and the relation set are finite
2. Every finite group is finitely presented
3. Some infinite groups are finitely presented (e.g., Z x Z = {x, y | xyx^{-1}y^{-1}})
4. A free group F_n is finitely presented (with no relations, or equivalently, with the empty relation set)
5. Not every group is finitely presented

# Construction / Recognition

## Standard Notation
- {x_1, ..., x_s | w_1, ..., w_t} denotes a finitely presented group
- The w_j are words in x_1, ..., x_s that equal the identity
- The vertical bar separates generators from relations

# Context & Application

Finitely presented groups are the groups that can be specified by a finite amount of data. Armstrong gives many examples: dihedral groups, cyclic groups, the quaternion group, wallpaper groups, and dicyclic groups are all finitely presented. The concept contrasts with free groups, which have no defining relations.

# Examples

**Example 1** (p. 176): D_n = {x, y | x^n, y^2, (xy)^2} -- finitely presented with 2 generators and 3 relations.

**Example 2** (p. 177): Q = {x, y | x^4, x^2y^{-2}, xyxy^{-1}} -- the quaternion group.

**Example 3** (p. 177): Z = {x | ---} -- finitely presented with 1 generator and 0 relations (a free group).

**Example 4** (p. 177): The free abelian group Z^n = {x_1,...,x_n | x_ix_jx_i^{-1}x_j^{-1}, 1 <= i < j <= n}.

# Relationships

## Builds Upon
- **Presentation of a group** -- Finite case of the general concept

## Related
- **Defining relations** -- The finite set of relator words

## Contrasts With
- **Free group** -- A free group has no defining relations (the relation set is empty)

# Common Errors

- **Error**: Assuming a finitely presented group must be finite
  **Correction**: Z = {x | ---} and Z x Z = {x, y | xyx^{-1}y^{-1}} are both infinite and finitely presented

# Common Confusions

- **Confusion**: Thinking "finitely generated" and "finitely presented" are the same
  **Clarification**: Finitely generated means finitely many generators; finitely presented additionally requires finitely many relations. A finitely generated group need not be finitely presented

# Source Reference

Chapter 27: Free Groups and Presentations, page 176 (pdf p. 176). Definition and notation.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 176
- Confidence: HIGH -- explicit definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
