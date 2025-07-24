'use client';

import { Button } from '@/app/components/ui/Button';

export type ChartType = 'bar' | 'line' | 'pie' | 'table';

interface ChartTypeSelectorProps {
  selectedType: ChartType;
  onTypeChange: (type: ChartType) => void;
  className?: string;
}

const chartTypes = [
  { type: 'bar' as ChartType, label: 'Bar Chart', icon: '📊' },
  { type: 'line' as ChartType, label: 'Line Chart', icon: '📈' },
  { type: 'pie' as ChartType, label: 'Pie Chart', icon: '🥧' },
  { type: 'table' as ChartType, label: 'Data Table', icon: '📋' },
];

export function ChartTypeSelector({ selectedType, onTypeChange, className }: ChartTypeSelectorProps) {
  return (
    <div className={`flex gap-2 ${className}`}>
      {chartTypes.map(({ type, label, icon }) => (
        <Button
          key={type}
          variant={selectedType === type ? 'primary' : 'outline'}
          size="sm"
          onClick={() => onTypeChange(type)}
          className="flex items-center gap-2"
        >
          <span>{icon}</span>
          <span className="hidden sm:inline">{label}</span>
        </Button>
      ))}
    </div>
  );
}
