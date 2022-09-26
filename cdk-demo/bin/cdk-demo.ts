#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { CdkDemoStack } from '../lib/cdk-demo-stack';

const app = new cdk.App();
new CdkDemoStack(app, 'CdkDemoStack', {
  env: { account: '161833304357', region: 'ap-northeast-1' },

});
