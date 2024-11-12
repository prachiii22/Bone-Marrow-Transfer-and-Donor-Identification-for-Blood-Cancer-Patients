import React from 'react';
import { View, Text, Button } from 'react-native';
import HomeScreen from './components/HomeScreen';

const App = () => {
  return (
    <View>
      <HomeScreen />
    </View>
  );
};

export default App;
HomeScreen.js
Create a basic home screen with navigation options.

js
Copy code
import React from 'react';
import { View, Text, Button } from 'react-native';

const HomeScreen = () => {
  return (
    <View>
      <Text>Welcome to the Bone Marrow Donor App</Text>
      <Button title="View Patients" onPress={() => {}} />
      <Button title="View Donors" onPress={() => {}} />
      <Button title="Match Donor" onPress={() => {}} />
    </View>
  );
};

export default HomeScreen;
