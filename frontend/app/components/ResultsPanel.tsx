"use client";

import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/Card";
import { ChartTypeSelector, ChartType } from "./charts/ChartTypeSelector";
import { DataVisualization } from "./charts/DataVisualization";

interface ResultsPanelProps {
  response: {
    data: Record<string, unknown>[];
    sql: string;
    question?: string;
    error?: string;
    type?: string;
    is_dummy?: boolean;
    warning?: string;
  };
  className?: string;
}

function detectBestChartType(data: Record<string, unknown>[]): ChartType {
  if (!data || data.length === 0) return "table";

  const keys = Object.keys(data[0]);
  if (keys.length !== 2) return "table";

  const secondKey = keys[1];
  const isNumeric = typeof data[0][secondKey] === "number";

  if (!isNumeric) return "table";

  // If we have time-based data, prefer line chart
  const firstKey = keys[0].toLowerCase();
  if (
    firstKey.includes("date") ||
    firstKey.includes("time") ||
    firstKey.includes("month") ||
    firstKey.includes("year")
  ) {
    return "line";
  }

  // For categorical data with few items, prefer pie chart
  if (data.length <= 6) {
    return "pie";
  }

  // Default to bar chart for most cases
  return "bar";
}

export function ResultsPanel({ response, className }: ResultsPanelProps) {
  const [selectedChartType, setSelectedChartType] = useState<ChartType>(() =>
    detectBestChartType(response.data),
  );

  const canVisualize =
    response.data &&
    response.data.length > 0 &&
    Object.keys(response.data[0]).length === 2 &&
    typeof response.data[0][Object.keys(response.data[0])[1]] === "number";

  return (
    <div className={className}>
      <Card className="mb-6">
        <CardHeader className="pb-4">
          <div className="flex items-center gap-2 mb-2">
            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
            <CardTitle className="text-lg">
              Results for: &quot;{response.question || "Your query"}&quot;
            </CardTitle>
          </div>
          <p className="text-sm text-gray-600">
            Based on your query, here&apos;s what the data shows...
          </p>

          {/* Dummy data warning */}
          {response.is_dummy && (
            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
              <div className="flex items-center gap-2">
                <div className="text-yellow-600">
                  <svg
                    className="w-5 h-5"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fillRule="evenodd"
                      d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z"
                      clipRule="evenodd"
                    />
                  </svg>
                </div>
                <div>
                  <p className="text-sm font-medium text-yellow-800">
                    Demo Mode
                  </p>
                  <p className="text-xs text-yellow-700">
                    {response.warning ||
                      "Using sample data - OpenAI API key not configured"}
                  </p>
                </div>
              </div>
            </div>
          )}
        </CardHeader>

        <CardContent>
          {response.error ? (
            <div className="mb-6">
              <div className="flex flex-col items-center justify-center p-8 bg-red-50 border border-red-200 rounded-lg">
                <div className="text-4xl mb-4">❌</div>
                <div className="text-lg font-medium text-red-800 mb-2">
                  Invalid Question
                </div>
                <div className="text-sm text-red-600 text-center max-w-md">
                  {response.error}
                </div>
                <div className="text-xs text-red-500 mt-2">
                  Please try asking a clear question about your data, such as
                  &quot;What are the top selling products?&quot; or &quot;Show
                  me sales by date&quot;.
                </div>
              </div>
            </div>
          ) : canVisualize ? (
            <div className="mb-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="font-medium text-gray-900">Visualization</h3>
                <ChartTypeSelector
                  selectedType={selectedChartType}
                  onTypeChange={setSelectedChartType}
                />
              </div>
              <DataVisualization
                data={response.data}
                chartType={selectedChartType}
                className="bg-gray-50 rounded-lg p-4"
              />
            </div>
          ) : null}

          {!response.error && !canVisualize && (
            <div className="mb-6">
              <h3 className="font-medium text-gray-900 mb-2">Raw Data</h3>
              <DataVisualization
                data={response.data}
                chartType="table"
                className="border rounded-lg overflow-hidden"
              />
            </div>
          )}

          {!response.error && (
            <div className="space-y-4">
              <div>
                <h3 className="font-medium text-gray-900 mb-2">
                  Generated SQL
                </h3>
                <div className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm font-mono overflow-x-auto">
                  <pre>{response.sql}</pre>
                </div>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
