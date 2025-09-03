import grpc
from concurrent import futures
from modules.grpc.generated import datanode_pb2 as pb2
from modules.grpc.generated import datanode_pb2_grpc as pb2_grpc

from modules.blocks.service import save_block, get_block
from core.config import settings


class DataNodeService(pb2_grpc.DataNodeServiceServicer):
    def UploadBlock(self, request, context):
        save_block(request.block_id, request.data)
        return pb2.UploadBlockResponse(message=f"Block {request.block_id} saved") # pyright: ignore[reportAttributeAccessIssue]

    def DownloadBlock(self, request, context):
        data = get_block(request.block_id)
        if not data:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Block not found")
            return pb2.DownloadBlockResponse()  # pyright: ignore[reportAttributeAccessIssue] # objeto vacío
        return pb2.DownloadBlockResponse(block_id=request.block_id, data=data) # pyright: ignore[reportAttributeAccessIssue]


def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DataNodeServiceServicer_to_server(DataNodeService(), server)
    server.add_insecure_port(f"[::]:{settings.GRPC_PORT}")
    server.start()
    print(f"[gRPC] DataNode {settings.DATANODE_ID} listening on port {settings.GRPC_PORT}")
    server.wait_for_termination()