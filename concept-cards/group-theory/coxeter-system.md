---
# === CORE IDENTIFICATION ===
concept: Coxeter System
slug: coxeter-system

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: coxeter-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 38
section: "Coxeter groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-presentation
extends: []
related:
  - coxeter-group
  - coxeter-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Coxeter system?"
  - "How is a Coxeter system defined by a matrix?"
---

# Quick Definition

A Coxeter system is a pair $(G, S)$ where $G$ is a group and $S$ is a set of generators subject only to relations $(st)^{m(s,t)} = 1$, where $m(s,s) = 1$, $m(s,t) \ge 2$ for $s \neq t$, and $m(s,t) = m(t,s)$.

# Core Definition

"A *Coxeter system* is a pair $(G, S)$ consisting of a group $G$ and a set $S$ of generators for $G$ subject only to relations of the form $(st)^{m(s,t)} = 1$" where the function $m: S \times S \to \mathbb{N} \cup \{\infty\}$ satisfies: $m(s,s) = 1$ for all $s$; $m(s,t) \ge 2$ for $s \neq t$; $m(s,t) = m(t,s)$. (Milne, p. 38)

When $m(s,t) = \infty$, no relation is imposed between $s$ and $t$.

# Prerequisites

- **Group presentation** — a Coxeter system is a specific type of presentation

# Key Properties

1. The group $G = \langle S \mid R \rangle$ where $R = \{(st)^{m(s,t)} \mid m(s,t) \neq \infty\}$
2. The cardinality of $S$ is called the rank of the Coxeter system
3. Since $m(s,s) = 1$, each generator $s$ has order dividing 2 in $G$ (in fact, exactly 2 by Theorem 2.16)
4. Theorem 2.16: the natural map $S \to G$ is injective, each $s$ has order 2, and $st$ has order $m(s,t)$

# Construction / Recognition

## A Coxeter System is Determined by:
1. A set $S$
2. A symmetric function $m: S \times S \to \mathbb{N} \cup \{\infty\}$ with $m(s,s) = 1$ and $m(s,t) \ge 2$ for $s \neq t$

# Context & Application

Coxeter systems provide a unified framework for studying reflection groups, dihedral groups, symmetric groups, and many other important families. They arise naturally in Lie theory and algebraic geometry.

# Examples

**Example 1** (p. 38): The only rank-1 Coxeter system is $(C_2, \{s\})$.

**Example 2** (p. 38): Rank-2 systems are indexed by $m(s,t) \ge 2$. For finite $m$: $G = \langle s, t \mid s^2, t^2, (st)^m \rangle \cong D_m$. For $m = \infty$: $G = \langle s, t \mid s^2, t^2 \rangle$ (infinite dihedral group).

# Relationships

## Builds Upon
- **group-presentation**

## Enables
- **coxeter-group** — the group part of a Coxeter system
- **coxeter-matrix** — encodes the function $m$

# Source Reference

Chapter 2, Section "Coxeter groups", pages 38-39.

# Verification Notes

- Definition source: Direct from p. 38
- Confidence: HIGH — explicit definition
- Uncertainties: None
