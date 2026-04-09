---
# === CORE IDENTIFICATION ===
concept: Group Presentation
slug: group-presentation

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 35
section: "Generators and relations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - presentation of a group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generators-and-relations
  - free-group
extends: []
related:
  - finitely-presented-group
  - coxeter-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group presentation?"
  - "What does the notation <X | R> mean?"
---

# Quick Definition

A presentation $(X, R)$ of a group $G$ consists of a generating set $X$ and a set of relations $R$ such that $G \cong F_X / \langle\!\langle R \rangle\!\rangle$. The group is denoted $\langle X \mid R \rangle$.

# Core Definition

"One also says that $(X, R)$ is a **presentation** for $G$, and denotes $G$ by $\langle X \mid R \rangle$." (Milne, p. 35)

The universal property (Proposition 2.8): for any group $H$ and map $\alpha: X \to H$ sending each relation to 1, there exists a unique homomorphism $G \to H$ extending $\alpha$.

# Prerequisites

- **Generators and relations** — a presentation specifies both
- **Free group** — the presentation defines a quotient of a free group

# Key Properties

1. $\langle X \mid R \rangle = F_X / \langle\!\langle R \rangle\!\rangle$
2. The universal property (2.8) characterizes the presented group
3. A group can have many different presentations
4. To show $\langle X \mid R \rangle \cong G$: construct a surjection $\langle X \mid R \rangle \to G$ and show both sides have the same order (or the map is injective)

# Construction / Recognition

## Strategy to Verify a Presentation (Example 2.9):
1. Show the generators of $G$ satisfy the relations $R$
2. By the universal property, get a surjective homomorphism $\langle X \mid R \rangle \to G$
3. Show $|\langle X \mid R \rangle| \le |G|$ by enumerating coset representatives
4. Conclude the map is bijective

# Context & Application

Presentations are the standard way to define groups in combinatorial and geometric group theory. Fundamental groups of topological spaces are naturally given by presentations.

# Examples

**Example 1** (p. 35, Example 2.9): $\langle a, b \mid a^n, b^2, baba \rangle \cong D_n$. Proof: $r, s \in D_n$ satisfy the relations, giving a surjection; the relations show $|\langle a, b \mid \ldots \rangle| \le 2n = |D_n|$.

**Example 2** (p. 35): $\langle a, b \mid a^2, b^2, (ab)^n \rangle \cong D_n$ via $a \mapsto s$, $b \mapsto t$.

**Example 3** (p. 35): Fundamental groups of surfaces have natural presentations (Examples 2.7e-g).

# Relationships

## Builds Upon
- **generators-and-relations**, **free-group**

## Enables
- **finitely-presented-group** — when $X$ and $R$ are finite
- **coxeter-system** — Coxeter groups are defined by specific presentations

# Common Errors

- **Error**: Assuming a presentation makes it easy to understand the group
  **Correction**: Even simple-looking presentations can define trivial, infinite, or very complex groups (Example 2.7d)

# Common Confusions

- **Confusion**: Thinking different presentations give different groups
  **Clarification**: The same group can have many presentations (e.g., $D_n$ has at least two: $\langle r, s \mid r^n, s^2, srsr \rangle$ and $\langle s, t \mid s^2, t^2, (st)^n \rangle$)

# Source Reference

Chapter 2, pages 35-36. Examples 2.7-2.10, Proposition 2.8.

# Verification Notes

- Definition source: Direct from p. 35
- Confidence: HIGH — explicit definition
- Uncertainties: None
