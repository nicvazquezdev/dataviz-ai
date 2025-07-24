"use client";

import { Input } from "./ui/Input";
import { Button } from "./ui/Button";

interface QueryInterfaceProps {
  onSubmit: (question: string) => void;
  isLoading: boolean;
  question: string;
  onQuestionChange: (question: string) => void;
}

export function QueryInterface({
  onSubmit,
  isLoading,
  question,
  onQuestionChange,
}: QueryInterfaceProps) {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (question.trim() && !isLoading) {
      onSubmit(question.trim());
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="shadow-lg bg-white p-8">
      <div className="flex flex-col gap-5">
        <Input
          placeholder="e.g., What were the 3 best-selling products in 2024?"
          value={question}
          onChange={(e) => onQuestionChange(e.target.value)}
          onKeyDown={handleKeyDown}
          className="flex-1 text-lg"
          icon={
            <svg viewBox="0 0 24 24" fill="none" className="w-4 h-4">
              <circle
                cx="11"
                cy="11"
                r="8"
                stroke="currentColor"
                strokeWidth="2"
              />
              <path
                d="m21 21-4.35-4.35"
                stroke="currentColor"
                strokeWidth="2"
              />
            </svg>
          }
        />
        <Button
          type="submit"
          isLoading={isLoading}
          disabled={!question.trim() || isLoading}
          size="lg"
        >
          ✨ Get Insights
        </Button>
      </div>
    </form>
  );
}
