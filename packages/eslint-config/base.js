import js from '@eslint/js';
import prettier from 'eslint-config-prettier/flat';
import tseslint from 'typescript-eslint';

/** Paths nothing should ever lint. Shared so every config ignores the same set. */
export const ignores = [
  '**/node_modules/**',
  '**/dist/**',
  '**/build/**',
  '**/out/**',
  '**/coverage/**',
  '**/.next/**',
  '**/.turbo/**',
  '**/*.tsbuildinfo',
  '**/next-env.d.ts',
];

/** Rules that hold in every app and package. */
export const sharedRules = {
  // Leading underscore is the escape hatch for a deliberately unused binding.
  '@typescript-eslint/no-unused-vars': [
    'error',
    {
      argsIgnorePattern: '^_',
      varsIgnorePattern: '^_',
      caughtErrorsIgnorePattern: '^_',
    },
  ],
  '@typescript-eslint/consistent-type-imports': [
    'error',
    { prefer: 'type-imports', fixStyle: 'inline-type-imports' },
  ],
  'no-console': ['warn', { allow: ['warn', 'error'] }],
  eqeqeq: ['error', 'always', { null: 'ignore' }],
};

/**
 * For plain TypeScript packages (packages/contracts, packages/domain).
 * `prettier` MUST stay last: it switches off every rule Prettier owns.
 */
export default tseslint.config(
  { ignores },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  { rules: sharedRules },
  prettier,
);
