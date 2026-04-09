---
# === CORE IDENTIFICATION ===
concept: Variable
slug: variable

# === CLASSIFICATION ===
category: formal-system
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Formalization of an Intuitionistic Theory of Types"
chapter_number: 2
pdf_page: 9
section: "2.1, 2.3.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "typed variable"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
extends: []
related:
  - dependence
  - variable-restrictions
  - mathematical-object
contrasts_with:
  - object-constant

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding dependent types?"
---

# Quick Definition

A variable in Martin-Lof's theory of types is a symbol that has a unique type associated with it and that serves simultaneously as a term of that type.

# Core Definition

Martin-Lof writes in Section 2.1: "There will be *variables* each of which has a unique type associated with it, and a term or type will always depend on a certain finite number of variables."

Section 2.3.1 states the formal rule: "If x is a variable of type A, then x is a term of type A. We are not allowed to introduce a variable x of type A unless x is distinct from all the variables on which the type A depends."

Additionally: "the type of a free variable must always be uniquely associated with the variable in question. We shall not care about the naming of bound variables."

# Prerequisites

- type: Every variable has a unique type associated with it.

# Key Properties

1. Every variable has exactly one type associated with it; the same variable symbol cannot be used with two different types.
2. A variable of type A is itself a term of type A (rule 2.3.1).
3. A variable x of type A may only be introduced if x is distinct from all variables on which A depends.
4. Free variables carry significance; bound variables are identified up to renaming (alpha-equivalence).
5. The binding operators are lambda-abstraction, Pi, and Sigma: all free occurrences of x in b[x] become bound in (lambda x)b[x], and similarly for (Pi x in A)B[x] and (Sigma x in A)B[x].

# Construction / Recognition

## To Construct/Create:
1. Choose a symbol x not already in use with a different type.
2. Specify a type A such that x does not appear among the variables on which A depends.
3. Then x is a variable of type A, and simultaneously a term of type A.

## To Identify/Recognize:
1. A variable is a symbol that appears in a term or type and has a uniquely associated type.
2. Free occurrences are those not bound by lambda, Pi, or Sigma.
3. Bound occurrences arise inside the scope of (lambda x), (Pi x in A), or (Sigma x in A).

# Context & Application

Variables are the most basic terms and the starting point for building all other terms through the introduction and elimination rules. The strict typing discipline for variables -- each variable has exactly one type -- is essential for the coherence of dependent types, where the type of one variable may depend on another variable.

# Examples

If x is a variable of type N (natural numbers), then x is a term of type N.

If x is a variable of type A and B[x] is a type depending on x, then one can form (lambda x)b[x], in which the free occurrences of x in b[x] become bound.

# Relationships

## Builds Upon
- type: A variable is always declared together with its type.

## Enables
- dependence: Variables are the atoms on which the notion of dependence is defined.
- pi-introduction-rule: Lambda-abstraction binds a variable.
- sigma-introduction-rule: Pairing uses a variable's type to form the Sigma type.

## Related
- mathematical-object: A variable of type A denotes an abstract object of the type denoted by A.

## Contrasts With
- object-constant: Constants have closed types; variables may have types that depend on other variables.

# Common Errors

- **Error**: Reusing the same variable symbol with two different types.
  **Correction**: Each variable must be uniquely associated with a single type. Use a fresh variable name when a different type is needed.

- **Error**: Introducing a variable x of type A when A depends on x.
  **Correction**: The type A must not depend on x itself; x must be distinct from all variables on which A depends.

# Common Confusions

- **Confusion**: Confusing free and bound variables.
  **Clarification**: A variable occurrence is free unless it is in the scope of a binding operator (lambda, Pi, or Sigma) for that variable. Bound variables can be renamed without changing meaning.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.1 (notational conventions) and Section 2.3.1 (variables as terms).

# Verification Notes

Confidence: high. The role and restrictions on variables are explicitly stated in Sections 2.1 and 2.3.1.
