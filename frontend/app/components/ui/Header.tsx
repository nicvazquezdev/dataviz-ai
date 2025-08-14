import Link from "next/link";
import React from "react";

export default function Header() {
  return (
    <header className="bg-white shadow-md sticky top-0 z-20">
      <div className="container mx-auto px-4 py-6">
        <Link href={"/"} className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-gradient-to-br from-blue-500 to-purple-600">
            ✨
          </div>
          <div>
            <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              HX AI
            </h1>
            <p className="text-sm text-gray-500">Ask questions, get insights</p>
          </div>
        </Link>
      </div>
    </header>
  );
}
