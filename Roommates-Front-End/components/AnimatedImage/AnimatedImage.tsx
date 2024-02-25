import React, {useRef, useEffect} from 'react';
import { Animated, Easing, SafeAreaView, StyleSheet, Text, TouchableHighlight, View } from 'react-native';





export const AnimatedImage= () => {
    let rotateValueHolder = new Animated.Value(0);

    useEffect(() => {
      
      const rotateData = rotateValueHolder.interpolate({
        inputRange: [0, 1],
        outputRange: ['0deg', '360deg'],
      });

      Animated.loop(
        Animated.timing(rotateValueHolder, {
          toValue: 4,
          duration: 5000,
          easing: Easing.linear,
          useNativeDriver: false,
        })
      ).start();
    }, []);
  
    const rotateData = rotateValueHolder.interpolate({
      inputRange: [0, 1],
      outputRange: ['0deg', '360deg'],
    });

  return (
    <SafeAreaView style={{flex: 1}}>
      <View style={styles.container}>
        <Text style={styles.titleText}>
          Mira como giraaaa copon
        </Text>
        <Animated.Image
          style={{
            width: 200,
            height: 200,
            transform: [{rotate: rotateData}],
          }}
          source={
            require('./logo512.png')
          }
        />        
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 20,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#C2C2C2',
    },
    titleText: {
      fontSize: 22,
      textAlign: 'center',
      fontWeight: 'bold',
      padding: 20,
    },
    textStyle: {
      textAlign: 'center',
      marginTop: 10,
    },
    buttonStyle: {
      fontSize: 16,
      color: 'white',
      backgroundColor: 'green',
      padding: 5,
      marginTop: 32,
      minWidth: 250,
    },
    buttonTextStyle: {
      padding: 5,
      color: 'white',
      textAlign: 'center',
    },
  });

export default AnimatedImage;
