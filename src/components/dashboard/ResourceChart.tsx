import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';
import { useSelector } from 'react-redux';
import { RootState } from '../../store';
import { formatNumber } from '../../utils/helpers';

const ResourceChart: React.FC = () => {
  const data = useSelector((state: RootState) => state.resources.data);

  const renderTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <div>
          <p>Date: {payload[0].payload.date}</p>
          <p>Available Resources: {formatNumber(payload[0].payload.value)}</p>
        </div>
      );
    }
    return null;
  };

  return (
    <LineChart width={800} height={400} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="date" />
      <YAxis dataKey="value" />
      <Tooltip content={renderTooltip} />
      <Line type="monotone" dataKey="value" strokeWidth={2} />
    </LineChart>
  );
};

export default ResourceChart;
