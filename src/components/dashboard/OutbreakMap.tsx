import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { useSelector } from 'react-redux';
import { RootState } from '../../store';
import { formatNumber } from '../../utils/helpers';

const OutbreakMap: React.FC = () => {
  const outbreaks = useSelector((state: RootState) => state.outbreaks.data);

  const position = outbreaks.reduce(
    (acc, curr) => ({
      lat: acc.lat + curr.latitude,
      lng: acc.lng + curr.longitude,
    }),
    { lat: 0, lng: 0 }
  );

  const averagePosition = {
    lat: position.lat / outbreaks.length,
    lng: position.lng / outbreaks.length,
  };

  return (
    <MapContainer center={averagePosition} zoom={5}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {outbreaks.map((outbreak) => (
        <Marker key={outbreak.id} position={[outbreak.latitude, outbreak.longitude]}>
          <Popup>
            <div>
              <h3>Outbreak Details</h3>
              <p>Location: {outbreak.location}</p>
              <p>Number of Cases: {formatNumber(outbreak.numberOfCases)}</p>
            </div>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default OutbreakMap;
