// declaration of functions

// data structure : before vertex shader (mesh info)
struct vertexInfo
{
    float3 position : POSITION;
    float2 uv: TEXCOORD0;
    float3 color : COLOR;
};

// data structure : vertex shader to pixel shader
// also called interpolants because values interpolates through the triangle
// from one vertex to another
struct v2p
{
    float4 position : SV_POSITION;
    float2 uv : TEXCOORD0;
    float3 color : TEXCOORD1;
};

// uniforms : external parameters
sampler2D MyTexture;
float2 UVTile;
float4x4 worldViewProjection;

// vertex shader function
v2p vertexShader(vertexInfo input)
{
    v2p output;
    output.position = mul(worldViewProjection, float4(input.position,1.0));
    output.uv = input.uv * UVTile;
    output.color = input.color;
    return output;
}

