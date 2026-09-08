import prettier from 'eslint-config-prettier/flat';
import globals from 'globals';
import tseslint from 'typescript-eslint';
import base, { ignores, sharedRules } from './base.js';

/**
 * NestJS API. Adds type-aware rules, which need a TypeScript program — the
 * consuming app must supply `parserOptions.tsconfigRootDir`, because a path
 * resolved from inside this package would point at the package, not the app.
 */
export default tseslint.config(
  { ignores: [...ignores, '**/eslint.config.mjs'] },
  ...base,
  ...tseslint.configs.recommendedTypeChecked,
  {
    languageOptions: {
      globals: { ...globals.node, ...globals.jest },
      sourceType: 'commonjs',
      parserOptions: { projectService: true },
    },
  },
  {
    rules: {
      ...sharedRules,

      // Nest resolves constructor dependencies from emitDecoratorMetadata,
      // which only records a RUNTIME import. `import type` erases it, and the
      // injected parameter silently becomes undefined at runtime.
      '@typescript-eslint/consistent-type-imports': 'off',

      // Warnings, not errors: these fire constantly against Express and
      // Prisma surfaces and would otherwise block every commit.
      '@typescript-eslint/no-floating-promises': 'warn',
      '@typescript-eslint/no-unsafe-argument': 'warn',
    },
  },
  prettier,
);
