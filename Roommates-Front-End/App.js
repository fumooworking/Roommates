import React, {useRef, useEffect} from 'react';
import { StatusBar } from 'expo-status-bar';
import { Animated, Image, StyleSheet, Text, View } from 'react-native';
import AnimatedImage from './components/AnimatedImage/AnimatedImage';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>Vamos Eduardo programameeee</Text>
      <Text>ROOMMATES</Text>
      <AnimatedImage style={{height: 300, width: 300}}/>  
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  titleText: {
    fontSize: 22,
    textAlign: 'center',
    fontWeight: 'bold',
    padding: 20,
  }
});
