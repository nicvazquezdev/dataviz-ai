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
        </CardHeader>

        <CardContent>
          {canVisualize && (
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
          )}

          <div className="space-y-4">
            <div>
              <h3 className="font-medium text-gray-900 mb-2">Generated SQL</h3>
              <div className="bg-gray-900 text-gray-100 p-4 rounded-lg text-sm font-mono overflow-x-auto">
                <pre>{response.sql}</pre>
              </div>
            </div>

            {!canVisualize && (
              <div>
                <h3 className="font-medium text-gray-900 mb-2">Raw Data</h3>
                <DataVisualization
                  data={response.data}
                  chartType="table"
                  className="border rounded-lg overflow-hidden"
                />
              </div>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
